from parente import Parente
import crud

def atualiza_parente(parente: Parente):
    for pai in parente.pais:
        Paux = crud.buscar_parente(pai)
        if Paux is not None:
            P = Parente(Paux.id, Paux.nome, Paux.pais, Paux.filhos, Paux.irmaos, Paux.conjuge)
            if parente.id not in P.filhos:
                P.filhos.append(parente.id)
                crud.atualizar_parente(P)

    for filho in parente.filhos:
        Faux = crud.buscar_parente(filho)
        if Faux is not None:
            F = Parente(Faux.id, Faux.nome, Faux.pais, Faux.filhos, Faux.irmaos, Faux.conjuge)
            if parente.id not in F.pais:
                F.pais.append(parente.id)
                crud.atualizar_parente(F)

    for irmao in parente.irmaos:
        Iaux = crud.buscar_parente(irmao)
        if Iaux is not None:
            I = Parente(Iaux.id, Iaux.nome, Iaux.pais, Iaux.filhos, Iaux.irmaos, Iaux.conjuge)
            if parente.id not in I.irmaos:
                I.irmaos.append(parente.id)
                crud.atualizar_parente(I)

    if parente.conjuge:
        Caux = crud.buscar_parente(parente.conjuge)
        if Caux is not None:
            C = Parente(Caux.id, Caux.nome, Caux.pais, Caux.filhos, Caux.irmaos, Caux.conjuge)
            if not C.conjuge:
                C.conjuge = parente.id
                crud.atualizar_parente(C)
