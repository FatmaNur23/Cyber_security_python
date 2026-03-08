class film_analiz:
    def film_analiz(self):
        import pandas as pd
    
        data={
            'Film:' ['Inception','Interstellar','The Dark Knight','Prestige','Tenet'],
            'Yönetmen:'['Nolan','Nolan','Nolan','Nolan','Nolan'],
            'Puan:'[8.8,8.6,9.0,8.5,7.4],
            'Yıl:'[2010,2014,2008,2006,2020]
        }
        df=pd.DataFrame(data)
    
        yüksek_df=df[df['Puan']>8.7]

        ortalama=df['Puan'].mean()

        df['Eskilik']=df['Yıl'].apply(lambda x:'Eski' if x<2015 else 'Yeni')

        print("Yüksek Puanlı Filmler:",yüksek_df)
        print("\nOrtalama Puan:",ortalama)
        print("Güncel hali:",df)






    




    

