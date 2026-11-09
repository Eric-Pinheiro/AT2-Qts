# Product Requirements Document (PRD) - Workstation Provisioning API

## Visão Geral
Aplicação web para registro e provisionamento inicial de workstations de TI, garantindo padronização de SO e integração com o sistema de inventário.

## Requisitos Não Funcionais (ISO/IEC 25010)
- **Eficiência de Performance:** A API deve suportar pelo menos 50 requisições por segundo (RPS) com p95 inferior a 500ms.
- **Usabilidade / Acessibilidade:** A interface deve seguir a diretriz WCAG 2.1 AA, permitindo navegação 100% via teclado.
- **Confiabilidade:** O sistema deve tratar falhas de comunicação com o sistema de inventário (Mock) sem expor stack traces.

## Rotas
- `GET /` : Retorna a interface web em HTML.
- `POST /api/provision` : Recebe payload JSON `{ "hostname": str, "os_version": str }` e registra a máquina.