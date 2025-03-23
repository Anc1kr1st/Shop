import pandas
from fpdf import FPDF

df = pandas.read_csv("articles.csv", dtype={"id": str})


class Shop:
    def __init__(self, article_id):
        self.article_id = article_id
        self.name = df.loc[df["id"] == self.article_id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.article_id, "price"].squeeze()

    def items(self):
        """Change number of items in stock"""
        in_stock = df.loc[df["id"] == self.article_id, "in stock"].squeeze()
        return in_stock


class Receipt:
    def __init__(self, article):
        self.article = article

    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.article.article_id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)

        pdf.output("receipt.pdf")



print(df)
article_ID = input("Choose an article to buy: ")
article = Shop(article_ID)
if article.items():
    receipt = Receipt(article)
    receipt.generate()
else:
    print("No such article in stock.")

