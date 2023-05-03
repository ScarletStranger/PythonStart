from random import randint


# У класса Chromosome будет три свойства:
# rating - рейтинг хромосомы
# size - размер хромосомы
# genes - массив генов хромосомы
class Chromosome:
    def __init__(self, size, gene_pool):
        self.rating = 0
        self.size = size
        self.genes = bytearray(size)
        if gene_pool is not None:
            self.set_random_genes(gene_pool)


# Функция генерации случайной хромосомы
# Принимает параметры:
# Длина хромосомы(size)
# Набор генов для создания хромосомы (gene_pool)

    def set_random_genes(self, gene_pool):
        gene_pool_range = len(gene_pool)
        for i in range(self.size):
            rand_pos = randint(0, gene_pool_range)
            self.genes[i] = gene_pool[rand_pos]


# Функция заполнения популяции
# Принимает параметры:
# Размер популяции(pop_size)
# Размер хромосомы(chromo_size)
# Генофонд(genes)
def create_population(pop_size, chromo_size, genes):
    population = [None] * pop_size
    for i in range(pop_size):
        population[i] = Chromosome(chromo_size, gene_pool)
        return population


# функция вычисления рейтинга
# Принимате параметры:
# Созданная популяция(population)
# Целевая хромосома(final_chromo)
def calc_rating(population, final_chromo):
    for chromo in population:
        chromo.rating = chromo.size
        for i in range(chromo.size):
            if chromo.genes[i] == final_chromo[i]:
                chromo.rating -= 1


# Сортировка хромосом по рейтингу(пузырьком)
def sort_population(population):
    size = len(population)
    repeat = True
    while (repeat):
        repeat = False
        for i in range(0, size - 1):
            bubble = population[i]
            if (bubble.rating > population[i+1].rating):
                population[i] = population[i+1]
                population[i+1] = bubble
                repeat = True


# Функция отбора по принципу наилучшего(элитизм)
# Принимате параметры:
# Созданная популяция(population)
# Выжившие образцы(survivors)
def select(population, survivors):
    size = len(survivors)
    for i in range(size):
        survivors[i] = population[i]


# Функция заполнения второй половины популяции потомками
# (родители остаются в первой половине)
# Принимате параметры:
# Половинная популяция(population)
# Родители(parents)
# Количество потомков(children_count)
def repopulate(population, parents, children_count):
    pop_size = len(population)
    while children_count < pop_size:
        p1_pos = get_parent_index(parents, None)
        p2_pos = get_parent_index(parents, p1_pos)
        p1 = parents[p1_pos]
        p2 = parents[p2_pos]
        population[children_count] = cross(p1, p2)
        population[children_count + 1] = cross(p2, p1)
        children_count += 2


# Фунцкия отбора пар родителей среди выживших
# Принимате параметры:
# Родители(parents)
def get_parent_index(parents, exclude_index):
    size = len(parents)
    while True:
        index = randint(0, size - 1)
        if exclude_index is None or exclude_index != index:
            return index


# Функция скрещивания двух родителей
# Каждая пара порождает двух потомков
# Принимате параметры:
# Хромосома первого родителя(chromo1)
# Хромосома второго родителя(chromo2)
def cross(chromo1, chromo2):
    size = chromo_size
    point = randint(0, size - 1)
    child = Chromosome(size, None)
    for i in range(point):
        child.genes[i] = chromo1.genes[i]
    for i in range(point, size):
        child.genes[i] = chromo2.genes[i]
    return child


# Функция мутации
# За 1 цикл мутирует 1 символ целевой строки
# Принимате параметры:
# Изменённая популяция(population)
# Количество хромосом(chromo_count)
# Количество генов(gene_count)
# Все возможные гены(gene_pool)
def mutate (population, chromo_count, gene_count, gene_pool):
    pop_size = len(population)
    gene_pool_size = len(gene_pool)
    for i in range(chromo_count):
        chromo_pos = randint(0, pop_size - 1)
        chromo = population[chromo_pos]
        for j in range(gene_count):
            gene_pos = randint(0, gene_pool_size - 1)
            gene = gene_pool[gene_pos]
            gene_pos = randint(0, chromo_size - 1)
            chromo.genes[gene_pos] = gene


# Функция вывода целевой популяции
def print_population(population):
    i = 0
    for chromo in population:
        i += 1
        print(str(i) + '. ' + str(chromo.rating) + ': ' + chromo.genes.decode())

# Генофонд - строка-справочник со всеми возможными генами.
# Его и целевую строку(хромосому) кодируют в байтовые массивы


gene_pool = bytearray(b'abcdefghijklmnopqrstuvwxyz ') # Набор генов для создания хромосомы
final_chromo = bytearray(b'conundrum')  # целевая строка

chromo_size = len(final_chromo)  # размер целевой строки
population_size = 20  # размер популяции


survivors = [None] * (population_size // 2) # Количество выживших по приципу элитизма
population = create_population(population_size, chromo_size, gene_pool)

iteration_count = 0 # счётчик поколений

while True:
    iteration_count += 1
    calc_rating(population, final_chromo)
    sort_population(population)
    print('*** ' + str(iteration_count) + ' ***')
    print_population(population)
    if population[0].rating ==0 :
        break

select(population, survivors)
repopulate(population, survivors, population_size // 2)
mutate(population, 10, 1, gene_pool) # мутация делается по 1 гену за цикл