class LockedClass:
    def __setattr__(self, attr, value):
        if not hasattr(self, 'first_name') and attr != 'first_name':
            raise AttributeError(f"Cannot add attribute '{attr}' to instance of LockedClass")
        super().__setattr__(attr, value)

