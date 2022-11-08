def main():
    try:
        tall=int(input('Oppgi et tall: '))
        dividert = 14/tall
        print(dividert)

    except Exception as err:
        print(err)
    else:
        print('Divisjonen gikk fint!')
    finally:
        print('Dette skriver jeg ut uansett om feil eller ikke!!!')

main()
