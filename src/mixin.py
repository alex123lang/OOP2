class MixinOutput:

    def __repr__(self):
        return f'Объект был создан. Атрибуты, которые были переданы: {', '.join(f'{i} = {j}' for i, j in self.__dict__.items())}'
