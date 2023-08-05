import json

from imgbeddings import imgbeddings
from PIL import Image
from sqlalchemy import JSON
from tabulate import tabulate

from dql.query import C, DatasetQuery, Object, UDFBase


class ImageEmbeddings(UDFBase):
    def __init__(self):
        super().__init__(
            self.embedding,
            (("embedding_json", JSON),),
            (Object(self.load_image),),
        )
        self.emb = imgbeddings()

    def embedding(self, img):
        emb = self.emb.to_embeddings(img)
        return (json.dumps(emb[0].tolist()),)

    def load_image(self, raw):
        img = Image.open(raw)
        img.load()
        return img


if __name__ == "__main__":
    #   - save as a new shadow dataset
    DatasetQuery(path="s3://ldb-public/remote/data-lakes/dogs-and-cats/").filter(
        C.name.glob("*cat*.jpg")
    ).limit(5).add_signals(ImageEmbeddings()).save("cats_with_embeddings")

    print(tabulate(DatasetQuery(name="cats_with_embeddings").results()[:5]))
