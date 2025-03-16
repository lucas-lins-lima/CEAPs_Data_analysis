# CEAPs_Data_analysis
Project carried out by FIAP analyzing the CEAPS (Quota for the Exercise of Parliamentary Activity by Senators). For those who don't know what CEAPS is, it contains all the expenses that Brazilian senators have declared, divided by year.

This database is using the month of March 2025 to perform the analyses, containing all the latest data available from the Brazilian Federal Senate.

This project is in the area of ​​data science, and consists of 7 days of actions to be carried out based on the data presented above.

First step: To download the CEAPS data, I created a file in Python that instructs how to download the tables in Excel. In this step, I will gather all the data by year and clean and transform the data. The results of the first stage are in the file "data_processed_cleaned" in binary file.

Second step: Data analysis. They are in a Python file.

Third step: Data analysis and results obtained.

I will leave my analysis below in Portugues:

A Cota para o Exercício da Atividade Parlamentar dos Senadores (CEAPS) é um recurso crucial que assegura a transparência e o bom uso de fundos públicos por parte dos senadores brasileiros. Realizei uma análise dos dados para a FIAP dos anos acumulados entre 2008 e 2025 que revelou padrões sazonais distintos e identificou senadores cujos reembolsos merecem destaque.


Ao longo dos anos, ficou evidente que o segundo semestre do ano se destaca consistentemente em termos de valores reembolsados. Mais especificamente, o 6º bimestre é notavelmente o período com as maiores declarações, seguido de perto pelos 4º e 5º bimestres. Já no contexto trimestral, o 4º trimestre é aquele que apresenta os valores mais altos de reembolso, com o 3º trimestre também apresentando números significativos. Entre todos os meses, dezembro (mês 12) lidera como o período de maior relevância, registrando os maiores valores reembolsados pelos senadores.
![Dispersão_Semestre_Reembolsos](https://github.com/user-attachments/assets/79a9947c-3527-4381-96ee-fffc2df27db0)
![Dispersão_Bimestre_Reembolsos](https://github.com/user-attachments/assets/d78a9d45-5fe8-4352-929f-32b2f91d333e)
![Dispersão_Trimestre_Reembolsos](https://github.com/user-attachments/assets/b8ea7abb-cf9b-4412-b242-d0e7843cf7ef)
![Dispersão_Mes_Reembolsos](https://github.com/user-attachments/assets/06746600-5d64-4045-b637-5fd05921a89d)
![Dispersão_Ano_Reembolsos](https://github.com/user-attachments/assets/4fadbfaf-bfe8-453f-b9a5-05a7b7510caf)


Os anos de 2015, 2016, 2017 e 2024 se destacaram por apresentarem reembolsos que superaram as médias anuais esperadas. Esses gastos esporádicos, embora não recorrentes, levantam um ponto de atenção para análises futuras e desvios indevidos. Dentro desses anos, destaca-se o reembolso extraordinário de Eduardo Amorim em agosto de 2015, que requer uma investigação mais profunda sobre as circunstâncias desses gastos.
![Capturar 6](https://github.com/user-attachments/assets/326cbc98-be31-49dc-a485-7c6c0fc5e781)


Entre os senadores, Eduardo Amorim, Styvenson Valentim, e Davi Alcolumbre emergem como as figuras de maior destaque no que tange a declarações de reembolso. Eduardo Amorim, em particular, lidera o ranking de reembolsos desde 2008, com a maioria dos altos valores dos senadores coincidentemente concentrados no mês de dezembro.
![Capturar 1](https://github.com/user-attachments/assets/43482cbb-f1cd-44fb-ad1d-659286a57900)
![Capturar 2](https://github.com/user-attachments/assets/95b7232b-a1c1-4f2d-b0e5-3d0270e0e58c)
![Capturar 3](https://github.com/user-attachments/assets/b230b36d-6237-4080-b79b-fefc77f46682)
![Capturar 4](https://github.com/user-attachments/assets/9dbcb2c6-df3d-4255-8308-a733f3b086c1)
![Capturar 5](https://github.com/user-attachments/assets/c99d00e2-54ed-4afd-8097-43e595ddb6ec)

Uma análise detalhada dos tipos de despesas revela que a locomoção, alimentação, combustíveis e hospedagem constituem uma parte significativa das declarações, especialmente no caso de Eduardo Amorim em agosto de 2015. Já Styvenson Valentim, em dezembro de 2022, e Davi Alcolumbre, em dezembro de 2017, também apresentaram gastos notáveis em suas declarações de material de consumo e passagens, o que nos proporciona uma visão mais granular sobre como a CEAPS é utilizada.
![Capturar 6](https://github.com/user-attachments/assets/4561c162-b80b-49f5-b0e9-27afaad3e0b5)
![Capturar 7](https://github.com/user-attachments/assets/042c466a-dbb5-4e3b-a5ce-e9b11913550a)
![Capturar 8](https://github.com/user-attachments/assets/d593faf0-81c0-4963-99f2-3557fc02c5e3)

De 2008 a 2025 o ranking top 10 das pessoas que declararam maiores valores de reembolso foram:

1. Eduardo Amorim
![Capturar 6](https://github.com/user-attachments/assets/68aac9d0-0bd3-447f-9283-639d21980c19)

2. Styvenson Valentim
![Capturar 7](https://github.com/user-attachments/assets/2b8945cf-3fd0-482e-977d-45e7c0eca128)

3. Davi Alcolumbre
![Capturar 8](https://github.com/user-attachments/assets/f78da2db-fe32-42a4-b607-cd2822f86b53)

4. Sérgio Petecão
![Capturar 9](https://github.com/user-attachments/assets/67760ae9-e475-49f6-ba7d-e5b469fe9b94)

5. Mozarildo Cavalcanti
![Capturar 10](https://github.com/user-attachments/assets/413f0d71-6249-4ba0-91ec-29b6ec50e20b)

6. Angelo Coronel
![Capturar 11](https://github.com/user-attachments/assets/d0f21eb5-6438-4834-af13-5f4c888301e1)

7. Mecias de jesus
![Capturar 12](https://github.com/user-attachments/assets/bea83e8c-1329-4f0f-b7b3-7362a13c04b1)

8. Paulo Paim
![Capturar 13](https://github.com/user-attachments/assets/ef5c12e5-b481-4e46-8d0e-1edce386e70c)

9. Vanessa Grazziotin
![Capturar 14](https://github.com/user-attachments/assets/dd98ba36-f7bf-40c1-a420-01ff0c640b9d)

10. Rose de Freitas
![Capturar 15](https://github.com/user-attachments/assets/21c6e5c6-460f-4b06-b5bf-e79a8db3b670)



Note: This document is updated with each new step of the project.
