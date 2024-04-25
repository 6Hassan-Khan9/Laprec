import pandas as pd

pd.set_option('display.max_colwidth', None)

laptops = pd.read_csv("data-cleaned.csv")

laptops.rename(columns={"Model": "model", "Price": "price", "Rating": "rating"}, inplace=True)

laptops.drop(columns=["secondary_storage_type"], inplace=True)

laptops.sort_values(by=["rating"], ascending=[False], inplace=True)

laptops = laptops.astype(str)

laptops["num_cores"] = laptops["num_cores"].apply(lambda x: x+"cores")
laptops["ram_memory"] = laptops["ram_memory"].apply(lambda x: x+"GB-RAM")
laptops["primary_storage_capacity"] = laptops["primary_storage_capacity"].apply(lambda x: x+"GB")
laptops["display_size"] = laptops["display_size"].apply(lambda x: x+"''")

laptops["tags"] = laptops[["brand", "processor_brand", "processor_tier", "num_cores", "ram_memory", "primary_storage_type",
                           "primary_storage_capacity", "gpu_brand", "gpu_type", "display_size"]].apply(lambda x: ' '.join(x), axis = 1)

laptops["id"] = laptops.index

new = laptops[["id", "model", "tags"]]
new.index = range(len(new))

# 
new.to_csv("models/laptops.csv")