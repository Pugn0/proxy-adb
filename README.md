# AndroidRootChecker

## Aviso Legal

Este projeto é fornecido "como está", sem garantias de qualquer tipo. Os desenvolvedores deste projeto não serão responsáveis por quaisquer danos diretos, indiretos, incidentais, especiais, exemplares ou punitivos decorrentes do uso do software ou código fornecido. Este projeto é apenas para fins educacionais e não deve ser usado para atividades ilegais ou maliciosas. O uso deste projeto é inteiramente por sua conta e risco.

## Sobre o Projeto
O AndroidRootChecker é uma ferramenta de linha de comando projetada para verificar o status de root em dispositivos Android conectados via ADB. Ele permite que desenvolvedores e técnicos testem a configuração de segurança e os privilégios de root dos dispositivos, fornecendo informações valiosas sobre a configuração e saúde do dispositivo Android.

## Recursos
- **Verificação de Root**: Testa e valida se um dispositivo Android está com root habilitado.
- **Testes de Modo Avião**: Verifica e altera o estado do modo avião através de comandos ADB.
- **Leitura e Gravação de IDs**: Lê e armazena o Android ID do dispositivo em um arquivo para futuras referências.
- **Resolução de Conectividade ADB**: Checa a conectividade ADB com o dispositivo Android.

## Requisitos
- Python 3.6 ou superior
- Bibliotecas: `subprocess`, `os`

## Instalação

Para instalar e executar o AndroidRootChecker, siga os passos abaixo:

1. (Opcional) Configure um ambiente virtual:
   ```bash
   python -m venv env
   source env/bin/activate  # No Windows use `env\Scripts\activate`
   
2. Clone o repositório:
   ```bash
   git clone https://github.com/Pugn0/AndroidRootChecker.git
   
3. Navegue até o diretório do projeto:
   ```bash
   cd AndroidRootChecker

4. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt

5. Execute o script:
   ```bash
   python main.py
   
## Agradecimentos
Agradecimentos a todos que contribuíram para o desenvolvimento desta ferramenta, especialmente à comunidade de desenvolvedores Python e aos contribuidores dos pacotes utilizados.

## Contato
- **E-mail**: pugno@x.com
- **Telegram**: [t.me/pugno_fc](https://t.me/pugno_fc)
