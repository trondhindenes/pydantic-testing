from models import SuperModel


def main():
    data_a = {
        "name": "peter",
        "created": "2023-10-25T07:59:58+02:00"
    }
    instance_a = SuperModel(**data_a)
    instance_a.name  # This will always work, because we've validated it


if __name__ == "__main__":
    main()