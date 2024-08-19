import pandas as pd
def save_diary_excel(path,diary):
    """
    Salvare file excel del riepilogo diario
    :param path: Percorso dove salvare il file excel
    :param diary: Oggetto diario che si vuole trasformare in excel
    :return: Ritorna un file xlsx con tutti gli eventi del diario
    """
    df = pd.DataFrame(diary)
    df = df.drop(columns=['calendar'])
    df.to_excel(path,index=False)



