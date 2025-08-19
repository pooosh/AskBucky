#!/usr/bin/env python3
"""
Check what's currently loaded in Qdrant Cloud database
"""

import os
from qdrant_client import QdrantClient
from qdrant_client.http import models

def main():
    # Get Qdrant connection details from environment
    qdrant_url = os.environ.get("QDRANT_URL")
    qdrant_api_key = os.environ.get("QDRANT_API_KEY")
    collection_name = os.environ.get("QDRANT_COLLECTION", "nlweb_documents")
    
    if not qdrant_url:
        print("❌ QDRANT_URL not found in environment")
        return
    
    print(f"🔗 Connecting to Qdrant Cloud at: {qdrant_url}")
    print(f"📊 Collection: {collection_name}")
    
    try:
        # Create client
        client = QdrantClient(url=qdrant_url, api_key=qdrant_api_key, timeout=30.0)
        
        # Check if collection exists
        try:
            collection_info = client.get_collection(collection_name)
            print(f"✅ Collection '{collection_name}' exists")
            print(f"📈 Total points: {collection_info.points_count}")
        except Exception as e:
            print(f"❌ Collection '{collection_name}' not found: {e}")
            return
        
        # Get all points with payload
        print("\n🔍 Fetching all points...")
        points = client.scroll(
            collection_name=collection_name,
            limit=100,  # Get first 100 points
            with_payload=True,
            with_vectors=False
        )[0]
        
        if not points:
            print("📭 No points found in collection")
            return
        
        print(f"\n📋 Found {len(points)} points:")
        
        # Group by sitetag
        sitetags = {}
        for point in points:
            sitetag = point.payload.get("sitetag", "unknown")
            if sitetag not in sitetags:
                sitetags[sitetag] = []
            sitetags[sitetag].append(point)
        
        print(f"\n🏷️ Points by sitetag:")
        for sitetag, point_list in sitetags.items():
            print(f"  {sitetag}: {len(point_list)} points")
            # Show sample sources
            sources = [point.payload.get("source", "unknown") for point in point_list[:3]]
            for source in sources:
                print(f"    - {source}")
            if len(point_list) > 3:
                print(f"    ... and {len(point_list) - 3} more")
        
        # Show total count
        total_points = client.count(
            collection_name=collection_name
        ).count
        print(f"\n📊 Total points in collection: {total_points}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 