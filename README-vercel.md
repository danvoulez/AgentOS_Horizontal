# Deploy no Vercel (Monorepo) — AgentOS Horizontal

Este projeto é um monorepo. Para implantar apenas o painel Next.js na Vercel:

## Arquivos incluídos

- **vercel.json**: configura o build e as rotas
- **package.json**: garante detecção do Node e scripts de build/start
- **.vercelignore**: ignora tudo exceto a pasta `panel/` e arquivos de configuração

## Passos

1. Commite estes arquivos na raiz do repositório GitHub.  
2. No Vercel, clique em **Import Project** e selecione o repositório.  
3. Na etapa de **Configuração**, certifique-se de:
   - **Root Directory**: deixe em branco (raiz)
   - **Framework Preset**: **Next.js** (deve detectar via vercel.json)
4. Veja as configurações de build:  
   - **Build Command**: `npm run build`  
   - **Output Directory**: `.next`
5. Clique em **Deploy**.  

## Teste

Acesse a URL gerada pelo Vercel e veja a aplicação do painel em produção.  
Se precisar apontar rotas ao backend (Railway), configure variáveis de ambiente no painel do Vercel.