# RAFAELIA CATALOGO REGIME INDEX

> Índice de regimes para o repositório `Catalogo-cosmologico`, focado em separar observação astronômica, dados declarados, lacunas de evidência e leitura simbólica.

## Função do repositório

```text
Catalogo-cosmologico = camada observacional inicial do ecossistema RAFAELIA/RLL.
```

O objetivo correto é transformar objetos, observações e tabelas em cadeia verificável.

---

## Regimes principais

| Regime | Descrição | Uso correto |
|---|---|---|
| `[DADO-DECLARADO]` | JSON, CSV ou tabela presente no repositório | registrar e validar formato |
| `[OBSERVAÇÃO-BRUTA]` | medida com data, hora, coordenada, instrumento e fonte | base para validação |
| `[LACUNA]` | arquivo citado mas ausente ou incompleto | corrigir antes de claim forte |
| `[CATÁLOGO]` | lista organizada de objetos celestes | manter fonte e data de atualização |
| `[SIMBÓLICO]` | interpretação poética/espiritual do objeto | preservar, mas separar de prova |
| `[VALIDAÇÃO]` | resultado com fonte externa, script, métrica e reprodutibilidade | pode sustentar afirmações técnicas |

---

## Cadeia mínima de custódia

Para cada objeto astronômico, exigir:

```text
1. designação;
2. fonte externa;
3. data/hora da observação;
4. coordenadas;
5. magnitude ou grandeza observável;
6. instrumento ou catálogo;
7. arquivo bruto;
8. hash;
9. script de validação;
10. status: declarado, parcial real ou validado.
```

---

## Lacuna observacional conhecida

O arquivo `data/rafaelia_planeta1.json` referencia:

```text
data/observacoes/RAFAELIA_planeta1_obs.csv
```

Se o CSV não estiver presente, o status do objeto deve permanecer como:

```text
[DADO-DECLARADO] + [LACUNA]
```

Não promover para `[VALIDAÇÃO]` sem o arquivo de observações ou fonte externa equivalente.

---

## Regra de integração com RLL

```text
Catálogo observa → RLL modela → métrica compara → status sobe ou desce.
```

---

## Tarefa pendente

- confirmar todos os arquivos citados no README e nos JSON;
- criar ou restaurar diretório `data/observacoes/` se houver dados reais;
- adicionar hashes e metadados;
- separar tabela simbólica de tabela observacional;
- preparar script de validação de formato.
