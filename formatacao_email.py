from datetime import datetime
import locale

class EmailFormatar:
    def __init__(self, remetente, destinatario, nome_remetente):
        self.remetente = remetente
        self.destinatario = destinatario
        self.nome_remetente = nome_remetente.title()
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
        self.data_atual = datetime.now().strftime("%d de %B de %Y").replace("marÃ§o", "Março")
        self.hora_atual = datetime.now().strftime("%H:%M")
    
    def gerar_tabela(self, categoria, lista_chamados):
        categoria = categoria.replace(" ", "&nbsp;")

        if not lista_chamados:
            return f"""
            <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; width: 90%; margin: 20px auto;">
                <tr>
                    <th style="background-color: #f0f0f0; font-size: 18px; font-weight: bold; text-align: left; white-space: nowrap; width: 200px;">{categoria}:</th>
                    <td style="text-align: left;">Nenhum</td>
                </tr>
            </table>
            """
        else:
            chamados_formatados = ", ".join(lista_chamados)
            return f"""
            <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; width: 90%; margin: 20px auto;">
                <tr>
                    <th style="background-color: #f0f0f0; font-size: 18px; font-weight: bold; text-align: left; white-space: nowrap; width: 200px;">{categoria}:</th>
                    <td style="text-align: left;">{chamados_formatados}</td>
                </tr>
            </table>
            """



    
    def formatar_email(
        self, 
        noc_list, soc_list, n1_palmas_list, n1_araguaina_list, dc_list, infra_list, telefonia_list, crp_list,
        noc_list_hj, soc_list_hj, n1_palmas_list_hj, n1_araguaina_list_hj, dc_list_hj, infra_list_hj, telefonia_list_hj, crp_list_hj,
        noc_list_st, soc_list_st, n1_palmas_list_st, n1_araguaina_list_st, dc_list_st, infra_list_st, telefonia_list_st, crp_list_st

    ):
        return f"""
        <html>
            <head>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
            </head>
            <body style="font-family: Arial, sans-serif; font-size: 14px; color: #333333; background-color: #f8f8f8;">
                <div style="text-align: center; background-color: #000; padding: 20px;">
                    <img src="https://ugc.production.linktr.ee/ef83339a-c17f-44fd-a29e-9bad99c63a07_IDX---Logo-1-vertical-cor-invertida.png?io=true&size=avatar-v3_0" alt="Logo IDX Datacenters" width="100" />
                </div>
                <div style="text-align: center; margin: 20px auto; font-size: 30px; font-weight: bold;">
                    Relatório Completo de Chamados - SLAs e Chamados Sem Técnico | {self.data_atual} {self.hora_atual}
                </div>

                <div style="background-color: #ff5757; color: white; text-align: center; padding: 10px; font-weight: bold; font-size: 22px; margin: 20px auto; width: 90%; display: flex; justify-content: center; align-items: center; height: 60px;">
                    SLAs Excedidos:
                </div>
                
                {self.gerar_tabela("NOC", noc_list)}
                {self.gerar_tabela("SOC", soc_list)}
                {self.gerar_tabela("Suporte Palmas", n1_palmas_list)}
                {self.gerar_tabela("Suporte Araguaína", n1_araguaina_list)}
                {self.gerar_tabela("Data Center", dc_list)}
                {self.gerar_tabela("Infraestrutura", infra_list)}
                {self.gerar_tabela("Telefonia", telefonia_list)}
                {self.gerar_tabela("CRP", crp_list)}

                <div style="background-color: #f8a12d; color: white; text-align: center; padding: 10px; font-weight: bold; font-size: 22px; margin: 20px auto; width: 90%; display: flex; justify-content: center; align-items: center; height: 60px;">
                    SLAs que Excederão Hoje ({datetime.now().strftime("%d/%m/%Y")}):
                </div>

                {self.gerar_tabela("NOC", noc_list_hj)}
                {self.gerar_tabela("SOC", soc_list_hj)}
                {self.gerar_tabela("Suporte Palmas", n1_palmas_list_hj)}
                {self.gerar_tabela("Suporte Araguaína", n1_araguaina_list_hj)}
                {self.gerar_tabela("Data Center", dc_list_hj)}
                {self.gerar_tabela("Infraestrutura", infra_list_hj)}
                {self.gerar_tabela("Telefonia", telefonia_list_hj)}
                {self.gerar_tabela("CRP", crp_list_hj)}

                <div style="background-color: #2b98fa; color: white; text-align: center; padding: 10px; font-weight: bold; font-size: 22px; margin: 20px auto; width: 90%; display: flex; justify-content: center; align-items: center; height: 60px;">
                    Chamados sem Técnico ({datetime.now().strftime("%d/%m/%Y")}):
                </div>

                {self.gerar_tabela("NOC", noc_list_st)}
                {self.gerar_tabela("SOC", soc_list_st)}
                {self.gerar_tabela("Suporte Palmas", n1_palmas_list_st)}
                {self.gerar_tabela("Suporte Araguaína", n1_araguaina_list_st)}
                {self.gerar_tabela("Data Center", dc_list_st)}
                {self.gerar_tabela("Infraestrutura", infra_list_st)}
                {self.gerar_tabela("Telefonia", telefonia_list_st)}
                {self.gerar_tabela("CRP", crp_list_st)}

                <br>
                <p><b>Cordialmente, </b><b>{self.nome_remetente}.</b><br> 
                IDX Data Centers & IT Services</p>
                <a href="mailto:{self.remetente}">{self.remetente}</a><br>
                <a href="https://www.idxdatacenters.com.br" target="_blank">www.idxdatacenters.com.br</a></p>
            
                <footer style="text-align: center; color: #888888; font-size: 12px; margin-top: 30px;">
                <p>&copy; {datetime.now().year} IDX Datacenters. Todos os direitos reservados.</p>
                </footer>
            </body>
        </html>
        """
