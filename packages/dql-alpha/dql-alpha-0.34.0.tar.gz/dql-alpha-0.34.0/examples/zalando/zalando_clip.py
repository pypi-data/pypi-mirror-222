"""
fashion-clip UDF, using the
[fashion-clip](https://pypi.org/project/fashion-clip/#description) package.

Generated embeddings are stored json-encoded.
"""
import json

from fashion_clip.fashion_clip import FashionCLIP
from PIL import Image
from sqlalchemy import JSON
from tabulate import tabulate

from dql.query import C, DatasetQuery, Object, UDFBase


class MyFashionClip(UDFBase):
    def __init__(self):
        super().__init__(
            self.fashion_clip,
            (("fclip", JSON),),
            (Object(self.load_image),),
            batch=20,
        )
        self.fclip = FashionCLIP("fashion-clip")

    def load_image(self, raw):
        img = Image.open(raw)
        img.load()
        return img

    def fashion_clip(self, images):
        embeddings = self.fclip.encode_images([img[0] for img in images], batch_size=1)
        emb_json = [(json.dumps(emb),) for emb in embeddings.tolist()]
        return emb_json


if __name__ == "__main__":
    #   - save as a new shadow dataset
    DatasetQuery(path="s3://dql-zalando-hd-resized/zalando-hd-resized/").filter(
        C.name.glob("*.jpg")
    ).limit(5).add_signals(MyFashionClip()).save("zalando_hd_emb")

    print(tabulate(DatasetQuery(name="zalando_hd_emb").results()[:5]))
