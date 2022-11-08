liste = ['a', 'bb', 'ccc']

for i in range(6):
    try:
        print(f'På plass nummer {i} ligger {liste[i]}')
    except:
        print(f'Noe gikk galt med i lik {i}')

        # hva skjer med break her?
