class Relatorio:
    def __init__(self, lista_chamados):
        self.lista_chamados = lista_chamados
        self.noc_list = []
        self.soc_list = []
        self.n1_palmas_list = []
        self.n1_araguaina_list = []
        self.n1_paraiso_list = []
        self.dc_list = []
        self.infra_list = []
        self.excluir_list = []
        self.analisar_observador_list = []
        self.telefonia_list = []
        self.crp_list = []
        self.spam_list= ["Relatório", "RELATORIO"]

    def categorias(self):

        for item in self.lista_chamados:
            chamado = item["numero"]
            observador = item["observador"]
            categoria = item["categoria"]
            titulo = item["titulo"]

            grupos_permitidos = ["Atendimento > TI > Suporte", "Atendimento > TI"]
            grupos_observador = [g.strip() for g in observador.split(",")]
            
            if "NOC" in observador:
                self.noc_list.append(chamado)
            elif "SOC" in observador and not any(spam in titulo for spam in self.spam_list):
                self.soc_list.append(chamado)
            elif any(spam in titulo for spam in self.spam_list):
                self.excluir_list.append(chamado)
            elif "DC" in observador:
                self.dc_list.append(chamado)
            elif "Araguaína" in observador:
                self.n1_araguaina_list.append(chamado)
            elif "CRP" in observador:
                self.crp_list.append(chamado)
            elif "Paraiso" in observador:
                self.n1_paraiso_list.append(chamado)
            elif "Infra" in categoria:
                self.infra_list.append(chamado) 
            elif "Telefonia" in categoria:
                self.telefonia_list.append(chamado)
            elif "Palmas" in observador and "Infraestrutura" not in categoria:
                self.n1_palmas_list.append(chamado)
            elif all(grupo in grupos_permitidos for grupo in grupos_observador) and len(grupos_observador) <= len(grupos_permitidos):
                self.analisar_observador_list.append(chamado)
            
    
    def get_relatorio(self):
        return {
            "NOC": self.noc_list,
            "SOC": self.soc_list,
            "N1 Palmas": self.n1_palmas_list,
            "N1 Araguaína": self.n1_araguaina_list,
            "N1 Paraiso": self.n1_paraiso_list,
            "DC": self.dc_list,
            "Infra": self.infra_list,
            "Telefonia": self.telefonia_list,
            "CRP": self.crp_list if self.crp_list else [],
            "Excluir": self.excluir_list,
            "Analisar Observador": self.analisar_observador_list
        }