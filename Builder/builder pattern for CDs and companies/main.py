from sony import Sony
from samsung import Samsung

if __name__ == "__main__":
    # flexible construction
    sony = Sony.create().build_sony_cd().show_items()
    samsung = Samsung.create().build_samsung_cd().show_items()
