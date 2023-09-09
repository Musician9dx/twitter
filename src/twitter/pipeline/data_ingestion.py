from twitter.components.data_ingestion import data_ingestion


def data_ingest():
    obj=data_ingestion()
    obj.cursor_pymongo()
    obj.fetch_data()
    obj.save_csv()




Ingest_Data=data_ingest