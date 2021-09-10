tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def result_generator(t, k):
    t = (el for el in t)
    k = (el for el in k)
    for result in zip(k, t):
        yield result[::-1]
    for rest in t:
        yield rest, None


res_gen = result_generator(tutors, klasses)
for i in res_gen:
    print(i)
