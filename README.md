# Resistor-Project: Ringer ML Orchestrator

Um orquestrador de Machine Learning construído para o treinamento de modelos Convolutional Neural Networks (CNN) focados em dados de anéis (Ringer). Esta estrutura foi desenhada especificamente para transicionar de notebooks experimentais para um ambiente escalável em clusters de High Performance Computing (HPC) que utilizam o gerenciador de filas Slurm.

## 🏗️ Estrutura do Projeto

A arquitetura do projeto foi dividida em módulos lógicos seguindo práticas de MLOps:

- `config/`: Templates JSON para configurações de experimentos e scripts de carregamento de módulos HPC.
- `src/data/`: Lógica para carregamento (via HDF5) e pré-processamento (ex: normalização, fatiamento de anéis) dos dados.
- `src/models/`: Fábrica de modelos de Deep Learning (ex: arquiteturas de 1D CNNs).
- `src/core/`: O coração do pipeline, contendo o engine de treinamento, K-Fold Stratified, e callbacks customizados como o cálculo do índice SP (Soma-Produto).
- `src/jobs/`: Gerador de scripts Slurm (`.sbatch`) baseados dinamicamente nos parâmetros do experimento.
- `src/analysis/`: Módulo encarregado da avaliação pós-treinamento, calculando métricas (ROC, AUC) e gerando gráficos automáticos.

## ⚙️ Instalação e Configuração

### 1. Configurar o Ambiente HPC

Antes de rodar no cluster, você precisa garantir que os módulos corretos serão carregados. Acesse e edite o arquivo `config/env_setup.sh` de acordo com os módulos instalados no seu cluster:

```bash
# Exemplo de edição no config/env_setup.sh
module load python/3.10
module load cuda/11.8
module load cudnn/8.6.0
source /caminho/para/seu/venv/bin/activate
```

### 2. Configurar o Experimento

Os hiperparâmetros da CNN, do pipeline de dados e os recursos que você requisita do HPC ficam centralizados em um arquivo de configuração JSON. Copie ou edite o arquivo `config/template.json` existente:

```json
{
    "experiment_name": "ringer_v2_training",
    "version": 2,
    "data": {
        "rings": 25,
        "path": "/caminho/real/do/seu/dataset.h5"
    },
    "training": {
        "batch_size": 2048,
        "epochs": 100,
        "k_folds": 10
    },
    "hpc": {
        "queue": "gpu",
        "nodes": 1,
        "time": "24:00:00"
    }
}
```

## 🚀 Como Executar

### Submetendo no Slurm (Modo Cluster)

Para gerar automaticamente um script de submissão e enviá-lo ao Slurm de forma transparente, use o utilitário na raiz do projeto:

```bash
./submit_job.py config/template.json
```

O script irá:
1. Ler suas configurações do JSON.
2. Gerar o arquivo `.sbatch` na mesma pasta com os recursos computacionais requisitados.
3. Executar o comando `sbatch` para você, enviando o trabalho à fila.

**Dica**: Para gerar o arquivo Slurm sem efetivamente submetê-lo à fila (apenas para conferência manual), adicione a flag `--dry-run`:

```bash
./submit_job.py config/template.json --dry-run
```

### Rodando Localmente (Sem Slurm)

Se estiver testando na sua máquina pessoal (ou direto num nó interativo do HPC), você pode pular a parte de submissão e chamar o script de treinamento de forma direta:

```bash
python src/core/trainer.py --config config/template.json
```

## 📊 Análises e Resultados

Sempre que o loop principal de treinamento finalizado via Slurm, o próprio arquivo submetido já é encarregado de invocar automaticamente as rotinas de cálculo do módulo de análises:

```bash
python src/analysis/metrics.py --config config/template.json
```

Os logs de execução ficarão salvos na pasta `logs/`, os modelos treinados serão alocados na pasta `results/` e os gráficos comparativos na pasta `plots/` após a finalização bem sucedida do job no cluster.