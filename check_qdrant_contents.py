#!/usr/bin/env python3
"""
Check what's currently loaded in Qdrant Cloud database
"""

import os
import sys
from qdrant_client import QdrantClient
from qdrant_client.http import models

def main():
    # Get environment variables
    qdrant_url = os.environ.get("QDRANT_URL")
    qdrant_api_key = os.environ.get("QDRANT_API_KEY")
    collection_name = os.environ.get("QDRANT_COLLECTION", "askbucky")
    
    if not qdrant_url:
        print("❌ QDRANT_URL not found in environment")
        return
    
    if not qdrant_api_key:
        print("❌ QDRANT_API_KEY not found in environment")
        return
    
    print(f"🔗 Connecting to Qdrant Cloud at: {qdrant_url}")
    
    try:
        client = QdrantClient(url=qdrant_url, api_key=qdrant_api_key, timeout=30.0)
        
        # Check if collection exists
        try:
            collection_info = client.get_collection(collection_name)
            print(f"📊 Collection: {collection_name}")
            print(f"✅ Collection '{collection_name}' exists")
            print(f"📈 Total points: {collection_info.points_count}")
        except Exception as e:
            print(f"❌ Collection '{collection_name}' not found: {e}")
            return
        
        print(f"\n🔍 Fetching all points...")
        
        # Get all points
        points = []
        offset = None
        limit = 100
        
        while True:
            response = client.scroll(
                collection_name=collection_name,
                limit=limit,
                offset=offset,
                with_payload=True,
                with_vectors=True
            )
            
            batch_points = response[0]
            points.extend(batch_points)
            
            offset = response[1]
            if offset is None:
                break
        
        print(f"\n📋 Found {len(points)} points:")
        
        # Check for None vectors
        none_vectors = 0
        valid_vectors = 0
        
        for point in points:
            if point.vector is None:
                none_vectors += 1
            else:
                valid_vectors += 1
        
        print(f"🔢 Vector status:")
        print(f"  ✅ Valid vectors: {valid_vectors}")
        print(f"  ❌ None vectors: {none_vectors}")
        
        if none_vectors > 0:
            print(f"\n⚠️  WARNING: {none_vectors} points have None vectors!")
            print("This will cause search to fail.")
        
        # Group by sitetag
        sitetags = {}
        for point in points:
            sitetag = point.payload.get("sitetag", "unknown")
            if sitetag not in sitetags:
                sitetags[sitetag] = []
            sitetags[sitetag].append(point)
        
        print(f"\n🏷️  Points by sitetag:")
        for sitetag, tag_points in sitetags.items():
            print(f"  {sitetag}: {len(tag_points)} points")
            
            # Show first few file paths
            for i, point in enumerate(tag_points[:3]):
                source = point.payload.get("source", "unknown")
                print(f"    - {source}")
            if len(tag_points) > 3:
                print(f"    ... and {len(tag_points) - 3} more")
        
        print(f"\n📊 Total points in collection: {len(points)}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 