# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BolagsplatsenScraperPipeline:
    def process_item(self, item, spider):
        return item


class MemoryCollectionPipeline:
    """Pipeline to collect items in memory for API responses"""
    
    def __init__(self):
        self.collected_items = []
    
    def process_item(self, item, spider):
        """Collect each item in memory"""
        import logging
        logger = logging.getLogger(__name__)
        logger.info(f"MemoryCollectionPipeline processing item: {type(item)}")
        self.collected_items.append(item)
        logger.info(f"MemoryCollectionPipeline now has {len(self.collected_items)} items")
        return item
    
    def get_collected_items(self):
        """Return all collected items"""
        return self.collected_items.copy()
    
    def clear_items(self):
        """Clear collected items"""
        self.collected_items.clear()
