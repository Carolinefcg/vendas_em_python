# Desenvoldo por CAROLINE FERREIRA DA CRUZ GOMES
# Este programa realiza o cadastro, a alteração e o relatório de vendas de inúmeros produtos
# Os arquvos serão salvos em .txt
# O código foi feito para ser facilmente lido pelo Excel (e similares)

matriz = []
vendas = ['\n----------------\nCliente', [], 'Data', [], '\nCodigo', 'Quantidade', [], [], 'Valor_da_venda', [], 'Valor_total', []]
erro = 0
cond = int(input('Para iniciar,\ndigite qualquer inteiro, exceto 0:'))
itens = ['Codigo', 'Descricao', 'Preco', 'Quantidade']
def entrada():  # funcao para receber os dados
    print('\nProduto', i + 1)
    f = open('inventario.txt', "r")
    lines = f.readlines()
    if len(lines) < 2:
        with open("inventario.txt", "a") as txt_file: # escrevendo a primeira linha na matriz do arquivo
            txt_file.write(" ".join(itens) + "\n")
    linha = []
    for j in range(4):  # 4 eh a quantidade de colunas
        linha.append((input(str(itens[j]))))
    matriz.append(linha)
    return matriz
def conferindo():  # conferindo todos os codigos ja inseridos
    f = open('inventario.txt', "r")
    mat_arq = []
    lines = f.readlines()
    for x in lines:
        mat_arq.append(x.split(' '))  # use para pegar a matriz txt
    return mat_arq
def cad_neg():  # se o cadastro for negado
    for k in range(len(m)):
        for q in range(1, len(r)):  # comeca do 1 pq a primeira linha da primeira coluna de r eh "codigo"
            if m[k][0] == r[q][0]:
                print('\n-------------------------------------------------')
                print('ATENCAO! Este codigo', m[k][0], 'ja existe para o produto', r[q][1],
                      '\nO cadastro foi negado.')
                print('-------------------------------------------------\n')
                m[k] = '0'
                continue
    return m
def cad():  # dando tudo ok, vai cadastrar
    with open("inventario.txt", "a") as txt_file:
        for b in range(len(m)):
            if m[b] != '0' and m[b] != '\n':
                txt_file.write(" ".join(matriz[b]) + "\n")
                print('**O produto de descricao', m[b][1], 'foi cadastrado com sucesso**\n')
                m[b] = '0'
                continue
def alt_cad():
    c1 = input('Digite o codigo do produto: ')
    achou = 0
    for e in range(len(r)):
        if c1 == r[e][0]:
            achou = 1
            print('O produto selecionado foi\nDescricao:', r[e][1], '\nPreco: R$'+r[e][2], '\nQuantidade:',r[e][3])
            print('\nALTERACAO\n')
            r[e][1] = input('Novo valor para a descricao: ')
            r[e][2] = input('Novo valor para o preco: ')
            r[e][3] = input('Novo valor para a quantidade: ')
            r[e][3] += '\n'# dando uma quebra de linha no final
            # salvando a nova matriz no txt
            open('inventario.txt', 'w').close()  # limpando o arquivo
            for b in range(len(r)):
                if r[b] != '0' and r[b] != '\n':
                    with open("inventario.txt", "a") as txt_file:
                        txt_file.write(" ".join(r[b]) + "")
            print('**O produto de descricao', r[e][1], 'foi alterado com sucesso\n')
    if achou == 0:
        print('O produto de codigo', c1, 'nao foi encontrado no inventario')
def venda_valida():
    valido_codigo = 0
    lugar_matriz = []# eh um vetor pois eh para saben o lugar da matriz de cada produto
    inicio = 1
    while inicio != 0:
        soma = 0
        vendas[1].append(str(input('Nome do cliente: ')))
        vendas[3].append(str(input('Data: ')))
        jk = int(input('Digite quantos itens serao vendidos: '))
        for jkk in range(jk):
            hk = jkk + 1
            vendas[6].append((input(str(hk) +'. Codigo do produto: ')))
            for gh in range(len(r)):  # conferir se o item desejado existe nos produtos cadastrados
                if vendas[6][(len(vendas[6]))-1] == r[gh][0]:  # procurando o codigo no vetor
                    valido_codigo = 1
                    lugar_matriz.append(gh)
                    continue
            if valido_codigo == 0:
                b = 'invalido'
                vendas[7].append(str(b))
                vendas[9].append(str(b))
                print('\nOperacao invalida\nO codigo', vendas[6][len(vendas[6])-1], 'nao existe nos produtos cadastrados\n')
                vendas[6][len(vendas[6])-1] = b
                break
            if valido_codigo == 1:
                print('\n----DISPONIVEL NO ESTOQUE----\nDescricao:', r[lugar_matriz[len(lugar_matriz)-1]][1], '\nPreco: R$' + r[lugar_matriz[len(lugar_matriz)-1]][2],'\nQuantidade:', r[lugar_matriz[len(lugar_matriz)-1]][3] + '---------------------------')
            vendas[7].append((input('Quantidade do item ' + vendas[6][len(vendas[6]) - 1] + ': ')))  # o codigo existindo, partimos para a quantidade
            valido_codigo = 0
            if int(vendas[7][len(vendas[7])-1]) <= int(r[lugar_matriz[len(lugar_matriz)-1]][3]) and  int(vendas[7][len(vendas[7])-1]) > 0:  # verificando se quantidade eh valida
                r[lugar_matriz[len(lugar_matriz) - 1]][3] = str(int(r[lugar_matriz[len(lugar_matriz) - 1]][3])-int(vendas[7][len(vendas[7])-1]))+'\n'
            else:
                vendas[7][len(vendas[7])-1] = 'invalido'
                print('\nOperacao invalida\nO produto de codigo', vendas[6][len(vendas[6])-1],
                      'possui quantidade inferior (ou nula) no estoque\n')
                vendas[6][len(vendas[6]) - 1] = 'invalido'
                vendas[9].append(str('invalido'))
                break
            valor_produto = float(r[lugar_matriz[len(lugar_matriz)-1]][2])  # se tudo ok, veja o valor da venda
            vendas[9].append(valor_produto*(float(vendas[7][len(vendas[7])-1])))
            print('Valor da venda do produto',r[lugar_matriz[len(lugar_matriz)-1]][1],': R$',vendas[9][len(vendas[9])-1])
        inicio= int(input('Para continuar, digite 1\nSenao, digite 0\n>>>'))
        if inicio == 1:
            print('-------------------')
            vendas[9].append(str('final'))# mostra ate onde a compra eh de tal cliente
            vendas[7].append(str('final'))  # mostra ate onde a compra eh de tal cliente
            vendas[6].append(str('final'))  # mostra ate onde a compra eh de tal cliente
            venda_validada = [lugar_matriz, vendas]
            continue
        else:
            print('-------FINAL DA OPERACAO---------')
            vendas[9].append(str('final'))  # mostra ate onde a compra eh de tal cliente
            vendas[7].append(str('final'))  # mostra ate onde a compra eh de tal cliente
            vendas[6].append(str('final'))  # mostra ate onde a compra eh de tal cliente
            venda_validada = [lugar_matriz, vendas]
            return venda_validada
def venda_cad():# cadastrando no arquivo txt
    finais = []
    soma = 0
    for i in range(len(venda_ok[1][9])):
        if venda_ok[1][9][i] == 'final':
            finais.append(i)  # pegando as posicoes no vetor venda_ok[1][9] em que cada cliente termina a sua compra
    if finais[0] == 1 and venda_ok[1][6][0] == 'invalido':
        venda_ok[1][1][0] = 'invalido'
    for g in range(len(venda_ok[1][1])):
        for k in range(1, len(finais)):
            for u in range(finais[k - 1], finais[k]):
                if (finais[k] - finais[k - 1] <= 2) and venda_ok[1][6][u] == 'invalido':
                    venda_ok[1][1][k] = 'invalido'
                    continue
    for k in range(len(venda_ok[1][1])): #fazendo por cliente
        soma = 0
        if venda_ok[1][1][k] != 'invalido': # se o cliente for valido
            with open("vendas.txt", "a") as txt_file:
                if venda_ok[1][1][k] != 'invalido':
                    txt_file.write("".join(venda_ok[1][0]) + " ")  # cliente
                    txt_file.write("".join(venda_ok[1][1][k] + "\n"))# nome do cliente
                    txt_file.write("".join(venda_ok[1][2]) + " ")# data
                    txt_file.write("".join(venda_ok[1][3][k]) + "")  # qual a data
                    txt_file.write("".join(venda_ok[1][4]) + " ")  # codigo
                    txt_file.write("".join(venda_ok[1][5]) + " ")  # Quantidade
                    txt_file.write("".join(str(venda_ok[1][8])) + "\n")  # Valor venda
            if k == 0:
                for i in range(finais[k]):  # produtos que um determinado cliente comprou
                    with open("vendas.txt", "a") as txt_file:
                        if venda_ok[1][6][i] != 'invalido' and venda_ok[1][7][i] != 'invalido' and venda_ok[1][9][i] != 'invalido' and venda_ok[1][6][i] != 'final' and venda_ok[1][7][i] != 'final':
                                txt_file.write("".join(venda_ok[1][6][i]) + " ")
                                txt_file.write("".join(venda_ok[1][7][i]) + " ")
                                txt_file.write("".join(str(venda_ok[1][9][i])) + "\n")
                                soma += float(venda_ok[1][9][i])
                                continue
                print('Venda realizada com sucesso')
                with open("vendas.txt", "a") as txt_file:
                    txt_file.write("".join(str(venda_ok[1][10])) + " ")
                    txt_file.write("".join(str(soma)) + "\n")
                    txt_file.write("".join('--------------') + "")
            else:
                with open("vendas.txt", "a") as txt_file:
                    for i in range(finais[k-1], finais[k]):  # produtos que um determinado cliente comprou
                        if venda_ok[1][9][i] != 'invalido' and venda_ok[1][6][i] != 'final' and venda_ok[1][7][i] != 'final' and venda_ok[1][6][i] != 'invalido' and venda_ok[1][7][i]!='invalido':
                                txt_file.write("".join(venda_ok[1][6][i]) + " ")
                                txt_file.write("".join(venda_ok[1][7][i]) + " ")
                                txt_file.write("".join(str(venda_ok[1][9][i])) + "\n")
                                soma += float(venda_ok[1][9][i])
                                continue
                    txt_file.write("".join(str(venda_ok[1][10])) + " ")
                    txt_file.write("".join(str(soma))+"\n")
                    txt_file.write("".join('--------------') + "")
                    print('Venda realizada com sucesso')
        open('inventario.txt', 'w').close()  # limpando o arquivo cadastro
        for b in range(len(r)):
                    if r[b] != '0' and r[b] != '\n':
                        with open("inventario.txt", "a") as txt_file:
                            txt_file.write(" ".join(r[b]) + "")
                            continue
def mostrar_inventario():
    dia_teve_vendas = 0
    if escolha == '1' and formato == '1':
        if len(r) <= 1:
            print('Nao ha produtor cadastrados\nNao foi possivel realizar a operacao')
        for i in range(len(r)):
            print(r[i])
            continue
        return
    if escolha == '1' and formato == '2':
        open('relatorio.txt', 'w').close()  # limpando o arquivo
        if len(r) <= 1:
            print('Nao ha produtor cadastrados\nNao foi possivel realizar a operacao')
        for b in range(len(r)):
            if r[b] != '0' and r[b] != '\n':
                with open("relatorio.txt", "a") as txt_file:
                    txt_file.write(" ".join(r[b]) + "")
        print('**O arquivo relatorio.txt contem as informacoes sobre o INVENTARIO')
        return
    if escolha == '2' and formato == '1':
        f = open('vendas.txt', "r")
        mat_vendas = []
        lines = f.readlines()
        if len(lines) <= 1:
            print('O arquivo vendas.txt nao possui registros')
        for x in lines:
            mat_vendas.append(x.split(' '))  # use para pegar a matriz txt
        data_hoje = input('\nDigite a data de hoje: ')+'\n'
        for k in range(len(mat_vendas)):
            if mat_vendas[k][0] == 'Data' and mat_vendas[k][1] == data_hoje:
                    dia_teve_vendas = 1
                    print(mat_vendas[k-2][0], end='')
                    print(mat_vendas[k-1][0], mat_vendas[k-1][1], end='')
                    print(mat_vendas[k][0], mat_vendas[k][1], end='')
                    print(mat_vendas[k+1][0], mat_vendas[k+1][1], mat_vendas[k+1][2])
                    for i in range(k+2, len(mat_vendas)):
                        if len(mat_vendas[i]) != 1:
                                if len(mat_vendas[i]) == 3:
                                    print(mat_vendas[i][0], mat_vendas[i][1], mat_vendas[i][2], end = '')
                                if len(mat_vendas[i]) == 2:
                                    print(mat_vendas[i][0], mat_vendas[i][1],  end='')
                                continue
                        else:
                            print('----------------\n')
                            break
        if dia_teve_vendas == 0:
            print('Nao ha vendas registradas no dia', data_hoje)
        dia_teve_vendas = 0
    if escolha == '2' and formato == '2':
        open('relatorio.txt', 'w').close()  # limpando o arquivo
        f = open('vendas.txt', "r")
        mat_vendas = []
        lines = f.readlines()
        if len(lines) <= 1:
            print('O arquivo vendas.txt nao possui registros')
        else:
            for x in lines:
                mat_vendas.append(x.split(' '))  # use para pegar a matriz txt
            data_hoje = input('\nDigite a data de hoje: ') + '\n'
            with open("relatorio.txt", "a") as txt_file:
                txt_file.write(" ".join(['RELATORIO', 'DE', 'VENDAS', 'DO', 'DIA', data_hoje])+ " ")
                for k in range(len(mat_vendas)):
                    if mat_vendas[k][0] == 'Data' and mat_vendas[k][1] == data_hoje:
                        dia_teve_vendas = 1
                        txt_file.write(" ".join(mat_vendas[k - 2]) + " ") #soh pra ficar bontio no arquivo
                        txt_file.write(" ".join(mat_vendas[k - 1]) + " ")
                        txt_file.write(" ".join(mat_vendas[k]) + " ")
                        txt_file.write(" ".join(mat_vendas[k+1]) + " ")
                        for i in range(k + 2, len(mat_vendas) - 2):
                            if mat_vendas[i][0] != '\n' and mat_vendas[i] != ['--------------\n']:
                                txt_file.write(" ".join(mat_vendas[i]) + " ")
                                continue
                            else:
                                txt_file.write(" ".join(['-------------\n']) + " ")
                                break
                if dia_teve_vendas == 0:
                    print('Nao ha vendas registradas em', data_hoje, '\n O arquivo relatoro.txt encontra-se vazio.')
                if dia_teve_vendas == 1:
                    print('**O arquivo relatorio.txt contem as informacoes sobre o Relatorio de vendas do dia', data_hoje)
    if escolha == '3' and formato == '1':
        f = open('vendas.txt', "r")
        mat_vendas = []
        lines = f.readlines()
        if len(lines) <= 1:
            print('O arquivo vendas.txt nao possui registros')
        for x in lines:
            mat_vendas.append(x.split(' '))  # use para pegar a matriz txt
        for k in range(len(mat_vendas)):
                if len(mat_vendas[k]) == 2:
                    print(mat_vendas[k][0], mat_vendas[k][1], end= '')
                elif len(mat_vendas[k]) == 3:
                    print(mat_vendas[k][0], mat_vendas[k][1], mat_vendas[k][2], end='')
                else:
                    print(mat_vendas[k][0])
    if escolha == '3' and formato == '2':
        open('relatorio.txt', 'w').close()  # limpando o arquivo
        f = open('vendas.txt', "r")
        mat_vendas = []
        lines = f.readlines()
        if len(lines) <= 1:
            print('O arquivo vendas.txt nao possui registros')
        else:
            for x in lines:
                mat_vendas.append(x.split(' '))  # use para pegar a matriz txt
            with open("relatorio.txt", "a") as txt_file:
                txt_file.write(" ".join(['RELATORIO', 'DE', 'VENDAS', 'GERAIS']) + " ")
                for k in range(len(mat_vendas)):
                        txt_file.write(" ".join(mat_vendas[k])+" ")
            print('**O arquivo relatorio.txt contem as informacoes sobre o Relatorio de vendas do dia')
    if escolha == '4' and formato == '1':
        f = open('vendas.txt', "r")
        mat_vendas = []
        lines = f.readlines()# no comeco, cod_prod tem valores zerados para todas as linhas da matriz
        prod = []
        maior_codigo = 0
        if len(lines) <= 1:
            print('O arquivo vendas.txt nao possui registros')
        for x in lines:
            mat_vendas.append(x.split(' '))  # use para pegar a matriz txt
        for k in range(len(mat_vendas)):
            if len(mat_vendas[k]) == 3 and mat_vendas[k][0] != 'Codigo':
                if int(mat_vendas[k][0]) > maior_codigo:
                    maior_codigo= int(mat_vendas[k][0])
                    continue
        cod_prod = [0] * (maior_codigo + 1)# todas as posicoes possiveis que cod_prod pode ter
        for j in range(len(mat_vendas)):
            if len(mat_vendas[j]) == 3 and mat_vendas[j][0] != 'Codigo':
                m = int(mat_vendas[j][0])
                qtd = int(mat_vendas[j][1])
                cod_prod[m] += qtd
                continue
        k = max(cod_prod)
        iguais = 0
        menor_qtd = []
        menor_p = []
        for i in range(len(cod_prod)):
            if k == cod_prod[i]:
                print('O produto com mais vendas foi o de codigo', i, 'com', k, 'unidades vendidas\n')
                iguais += 1
                continue
        if iguais > 1:
            print('Houve empate!\n')
        iguais = 0
        for i in range(1, len(cod_prod)):
            if cod_prod[i] > 0:
                menor_p.append(i)# codigo
                menor_qtd.append(cod_prod[i])# quantidade
        for i in range(len(menor_p)):
            if min(menor_qtd) == menor_qtd[i]:
                print('O produto que foi menos vendido foi o de codigo', menor_p[i],'com', menor_qtd[i],'unidades vendidas\n')
                iguais += 1
        if iguais > 1:
            print('Houve empate!')
    if escolha == '4' and formato == '2':
        f = open('vendas.txt', "r")
        mat_vendas = []
        lines = f.readlines()# no comeco, cod_prod tem valores zerados para todas as linhas da matriz
        prod = []
        maior_codigo = 0
        if len(lines) <= 1:
            print('O arquivo vendas.txt nao possui registros')
        for x in lines:
            mat_vendas.append(x.split(' '))  # use para pegar a matriz txt
        open('relatorio.txt', 'w').close()  # limpando o arquivo
        with open("relatorio.txt", "a") as txt_file:
            txt_file.write(" ".join(['PRODUTOS', 'MAIS', 'VENDIDOS']) + "\n")
            for k in range(len(mat_vendas)):
                if len(mat_vendas[k]) == 3 and mat_vendas[k][0] != 'Codigo':
                    if int(mat_vendas[k][0]) > maior_codigo:
                        maior_codigo= int(mat_vendas[k][0])
                        continue
            cod_prod = [0]*(maior_codigo+1) #todas as posicoes possiveis que cod_prod pode ter
            for j in range(len(mat_vendas)):
                if len(mat_vendas[j]) == 3 and mat_vendas[j][0] != 'Codigo':
                    m = int(mat_vendas[j][0])
                    qtd = int(mat_vendas[j][1])
                    cod_prod[m] += qtd
                    continue
            k = max(cod_prod)
            iguais = 0
            menor_qtd = []
            menor_p = []
            for i in range(len(cod_prod)):
                if k == cod_prod[i]:
                    txt_file.write(" ".join(['Codigo: ', str(i), '|| Unidades','vendidas:', str(k)]) + "\n\n")
                    iguais += 1
                    continue
            if iguais > 1:
                txt_file.write(" ".join(['Houve', 'empate!']) + "\n")
            iguais = 0
            txt_file.write(" ".join(['PRODUTOS', 'MENOS', 'VENDIDOS',]) + "\n")
            for i in range(1, len(cod_prod)):
                if cod_prod[i] > 0:
                    menor_p.append(i)#codigo
                    menor_qtd.append(cod_prod[i])#quantidade
            for i in range(len(menor_p)):
                if min(menor_qtd) == menor_qtd[i]:
                    txt_file.write(" ".join(['Codigo:', str(menor_p[i]), '|| Unidades', 'vendidas:', str(menor_qtd[i])]) + " ")
                    iguais += 1
            if iguais > 1:
                txt_file.write(" ".join(['Houve', 'empate!']) + "\n")
        print('**O arquivo relatorio.txt contem as informacoes sobre os produtos mais e menos vendidos')
    if escolha == '5' and formato == '1':
        f = open('vendas.txt', "r")
        mat_vendas = []
        lines = f.readlines()  # no comeco, cod_prod tem valores zerados para todas as linhas da matriz
        if len(lines) <= 1:
            print('O arquivo vendas.txt nao possui registros')
        for x in lines:
            mat_vendas.append(x.split(' '))  # use para pegar a matriz txt
        valores_venda = []
        clientes = []
        cliente_igual = 0
        contei = 0
        for i in range(len(mat_vendas)):
            for k in range(len(clientes)):
                if mat_vendas[i][0] == 'Cliente' and mat_vendas[i][1] == clientes[k]: # se for o mesmo cliente
                    cliente_igual += 1
                    for g in range(i, len(mat_vendas)):
                        if mat_vendas[g][0] == 'Valor_total' and contei == 0:
                            a = mat_vendas[g][1]
                            valores_venda[k] += float(a[:-1]) # acrescentou os valores totais do mesmo cliente
                            cliente_igual += 1
                            mat_vendas[g][0] = ''
                            mat_vendas[g][1] = ''
                            contei = 1
                            continue
                    contei = 0
            if mat_vendas[i][0] == 'Cliente' and cliente_igual == 0:
                clientes.append(str(mat_vendas[i][1]))
            if mat_vendas[i][0] == 'Valor_total' and cliente_igual == 0:
                a = mat_vendas[i][1]
                valores_venda.append(float(a[:-1]))
            cliente_igual = 0
        maximo = max(valores_venda)
        for i in range(len(clientes)):
            if maximo == valores_venda[i]:
                a = clientes[i]
                print('O cliente que mais comprou foi', str(a[:-1]), 'pagando R$', maximo)
                continue
    if escolha == '5' and formato == '2':
        f = open('vendas.txt', "r")
        mat_vendas = []
        lines = f.readlines()
        if len(lines) <= 1:
            print('O arquivo vendas.txt nao possui registros')
        for x in lines:
            mat_vendas.append(x.split(' '))  # use para pegar a matriz txt
        open('relatorio.txt', 'w').close()  # limpando o arquivo
        with open("relatorio.txt", "a") as txt_file:
            txt_file.write(" ".join(['CLIENTES', 'QUE', 'MAIS', 'COMPRARAM']) + "\n")
            valores_venda = []
            clientes = []
            cliente_igual = 0
            contei = 0
            for i in range(len(mat_vendas)):
                for k in range(len(clientes)):
                    if mat_vendas[i][0] == 'Cliente' and mat_vendas[i][1] == clientes[k]: # se for o mesmo cliente
                        cliente_igual += 1
                        for g in range(i, len(mat_vendas)):
                            if mat_vendas[g][0] == 'Valor_total' and contei == 0:
                                a = mat_vendas[g][1]
                                valores_venda[k] += float(a[:-1]) # acrescentou os valores totais do mesmo cliente
                                cliente_igual += 1
                                mat_vendas[g][0] = ''
                                mat_vendas[g][1] = ''
                                contei = 1
                                continue
                        contei = 0
                if mat_vendas[i][0] == 'Cliente' and cliente_igual == 0:
                    clientes.append(str(mat_vendas[i][1]))
                if mat_vendas[i][0] == 'Valor_total' and cliente_igual == 0:
                    a = mat_vendas[i][1]
                    valores_venda.append(float(a[:-1]))
                cliente_igual = 0
            maximo= max(valores_venda)
            for i in range(len(clientes)):
                if maximo == valores_venda[i]:
                    a = clientes[i]
                    txt_file.write(" ".join(['O', 'cliente', 'que', 'mais', 'comprou', 'foi:', str(a[:-1]), 'pagando', 'R$', str(maximo)]) + "\n")
                    continue
            print('**O arquivo relatorio.txt contem as informacoes sobre os clientes que mais compraram')
while cond != 0:
    arquivo = open('./inventario.txt', 'a')
    e = int(input('\nDigite o numero da operacao\n' +
                  '1. Cadastro de Produtos\n' +
                  '2. Alteracao de Cadastro\n' +
                  '3. Venda de Produtos\n' +
                  '4. Emissao de Relatorios\n' +
                  '>>>> '))
    while e == 1:
        print('\nCADASTRO DE PRODUTOS\n')
        n = int(input('Digite quantos produtos voce vai adicionar: '))
        for i in range(n):  # recebendo as linhas
            m = entrada()
            r = conferindo()
            cad_neg()
            cad()
        cond = int(input('\nDeseja continuar com o Cadastro de Produtos?\n'
                         'Voltar para o menu, digite 5\n'
                         'Continuar com o cadastro, digite 1 \n'
                         'Sair,  digite 0\n'
                         '>>>>'))
        if cond == 1:
            e = 1
            continue
        else:
            break
    while e == 2:
        print('\nALTERACAO DE PRODUTOS\n')
        r = conferindo()
        alt_cad()
        cond = int(input('\nDeseja continuar com a Alteracao de Produtos?\n'
                         'Voltar para o menu, digite 5\n'
                         'Continuar com a alteracao, digite 2 \n'
                         'Sair,  digite 0\n'
                         '>>>>'))
        if cond == 2:
            e = 2
            continue
        else:
            break
    while e == 3:
        e = 3
        print('\nVENDA DE PRODUTOS\n')
        r = conferindo()
        venda_ok = venda_valida()
        venda_cad()
        cond = int(input('\nDeseja continuar com a Venda de Produtos?\n'
                         'Voltar para o menu, digite 5\n'
                         'Continuar com a venda, digite 2 \n'
                         'Sair,  digite 0\n'
                         '>>>>'))
        if cond == 3:
            e = 3
            continue
        else:
            break
    while e == 4:
        e = 4
        print('\nEMISSAO DE RELATORIOS\n')
        r = conferindo()
        escolha = input('Inventario, digite 1\n'
                        'Relatorio de vendas do dia, digite 2\n'
                        'Relatorio de vendas geral, digite 3\n'
                        'Relatorio dos itens mais e menos vendidos, digite 4\n'
                        'Relatorio de clientes que mais compram, digite 5\n'
                        '>>>>')
        formato = input('Para ser impresso na tela, digite 1\n'
                        'Para ser impresso em arquivo .txt, digite 2\n'
                        '>>>>')
        mostrar_inventario()
        cond = int(input('\nDeseja continuar com a Emissao de Relatorios?\n'
                         'Voltar para o menu, digite 5\n'
                         'Continuar, digite 4 \n'
                         'Sair,  digite 0\n'
                         '>>>>'))
        if cond == 4:
            e = 4
            continue
        else:
            break