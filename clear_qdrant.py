#!/usr/bin/env python3
"""
Clear all points from Qdrant collection
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
        
        # Get current count
        total_points = client.count(collection_name=collection_name).count
        print(f"📊 Current points in collection: {total_points}")
        
        if total_points == 0:
            print("✅ Collection is already empty")
            return
        
        # Clear all points
        print("🗑️ Clearing all points...")
        points = client.scroll(collection_name=collection_name, limit=1000)[0]
        point_ids = [point.id for point in points]
        client.delete(
            collection_name=collection_name,
            points_selector=models.PointIdsList(points=point_ids)
        )
        
        # Verify deletion
        new_count = client.count(collection_name=collection_name).count
        print(f"✅ Successfully cleared collection. New count: {new_count}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 