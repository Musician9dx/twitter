from twitter.components.data_transformation import data_transformation as data_transformer

def data_transform():
    obj=data_transformer()
    obj.fetch_data()
    obj.data_wrangling()
    obj.tokeize_data()
    obj.save_csv()

data_transformation=data_transform