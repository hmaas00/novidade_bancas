import pandas as pd 

def get_pages(org):

    df = pd.read_csv('pages.csv')
 
    return df[df.org == org].page.values

if __name__ == "__main__":

    print(get_pages('fgv'))