from products.models import Product


def main():
    try:
        if not Product.objects.all().exists():
            products_data = [
                {'name': 'A Nice Ebook',
                 'price': 100
                 },
                {'name': 'A Wood Table',
                 'price': 100
                 },
                {'name': 'A Big TV',
                 'price': 100
                 },
                {'name': 'A too-small T-Shirt',
                 'price': 100
                 },
                {'name': 'A Beautiful Star',
                 'price': 100
                 },
                {'name': 'Me',
                 'price': 99999999
                 },
            ]
            for data in products_data:
                product = Product(name=data['name'], price=data['price'])
                product.save()
        print("Done")
    except Exception as err:
        print("?", err)
    return


if __name__ == '__main__':
    main()
