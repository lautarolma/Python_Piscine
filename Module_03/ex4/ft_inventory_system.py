import sys


def main() -> None:
    inventory: dict[str, int] = {}
    args = sys.argv[1:]
    for arg in args:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item, raw_quantity = arg.split(":", 1)
        if item in inventory:
            print((f"Redundant item '{item}' - discarding"))
            continue
        try:
            quantity = int(raw_quantity)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            continue
        inventory[item] = int(quantity)
    total_qty = sum(inventory.values())
    if total_qty == 0:
        return print("Inventory is empty — nothing to analyze.")

    print(f"Got inventory: {inventory}")
    print(f"Item list: {inventory.keys()}")
    n_items = len(inventory.values())
    print(f"Total quantity of the {n_items} items: {total_qty}")
    first_item = list(inventory.keys())[0]
    max_item = first_item
    for item in inventory.keys():
        percentage = (inventory[item] / total_qty) * 100
        print(f"Item {item} represents {round(percentage, 1)}%")
    for item in inventory.keys():
        if inventory[item] > inventory[max_item]:
            max_item = item
    print(
            f"Item most abundant: {max_item} with"
            f" quantity {inventory[max_item]}"
    )
    min_item = first_item
    for item in inventory.keys():
        if inventory[item] < inventory[min_item]:
            min_item = item
    print(
            f"Item least abundant: {min_item} with "
            f"quantity {inventory[min_item]}"
    )
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()

# He de tomar nota del caso de la iniciacion a None, que ha de ser
# verificada en cada ocasion que se utilize esta variable con posterioridad
# (en este caso respecto a su uso como indice, una vez inicialiazada.
# mypy desconoce esta instancia y retorna error si no hay un checker
# especifico de "if variable is not None:" en cada implementacion posterior.
# Para este caso en especifico he reemplazado la inicializacion de la Key
# del diccionario a la primer key del mismo, para evitar preinicialiazarla
# a None. Para esto he tenido que primero castear la lista de llaves del
# dictionary a list, para poder acceder por el indice [0] al primer
# elemento (diccionarios no son accesibles por indice).
