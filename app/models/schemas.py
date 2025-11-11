from pydantic import BaseModel
from typing import Optional, List


class DeputadoBase(BaseModel):
    id: int
    nome: str
    sigla_partido: Optional[str] = None
    sigla_uf: Optional[str] = None
    url_foto: Optional[str] = None


class DeputadoResponse(DeputadoBase):
    pass


class DeputadoDetalhadoResponse(BaseModel):
    id: int
    nome: str
    sigla_partido: Optional[str] = None
    sigla_uf: Optional[str] = None
    url_foto: Optional[str] = None
    email: Optional[str] = None
    data_nascimento: Optional[str] = None
    escolaridade: Optional[str] = None
    municipio_nascimento: Optional[str] = None
    uf_nascimento: Optional[str] = None


class DespesaBase(BaseModel):
    ano: int
    mes: int
    tipo_despesa: Optional[str] = None
    valor_documento: Optional[float] = None
    valor_liquido: Optional[float] = None
    fornecedor: Optional[str] = None


class DespesaResponse(DespesaBase):
    pass


class DespesasDeputadoResponse(BaseModel):
    deputado_id: int
    deputado_nome: str
    ano: int
    total_gastos: float
    despesas: List[DespesaResponse]


class VotoResponse(BaseModel):
    deputado_id: int
    deputado_nome: str
    sigla_partido: Optional[str] = None
    sigla_uf: Optional[str] = None
    voto: Optional[str] = None


class VotacaoVotosResponse(BaseModel):
    votacao_id: int
    votos: List[VotoResponse]


class TopGastosItem(BaseModel):
    deputado_id: int
    deputado_nome: str
    sigla_partido: Optional[str] = None
    sigla_uf: Optional[str] = None
    total_gastos: float


class TopGastosResponse(BaseModel):
    ano: int
    limite: int
    resultados: List[TopGastosItem]


class PaginatedResponse(BaseModel):
    dados: List[DeputadoResponse]
    pagina: int
    itens: int
    total: Optional[int] = None

