# ESP32C3-MaltingControl

Este repositório contém o código-fonte desenvolvido para o microcontrolador ESP32-C3, que atua como o controlador do malteador laboratorial de grãos. O código é responsável por gerenciar a comunicação Bluetooth com o aplicativo Android, além de controlar todo o processo de malteação.

## Sobre o Projeto

O **ESP32C3-MaltingControl** é o firmware desenvolvido para o microcontrolador ESP32-C3, que gerencia a lógica do malteador de grãos. Ele se comunica com o aplicativo Android via Bluetooth Low Energy (BLE), recebendo comandos e enviando dados em tempo real, como leituras de sensores e status do processo.

Este projeto faz parte do meu Trabalho de Conclusão de Curso (TCC) em Química Industrial e tem como objetivo principal fornecer uma solução de controle automatizado para o processo de malteação.

## Funcionalidades (em desenvolvimento)

- **Comunicação Bluetooth (BLE):**
  - Recebimento de comandos (start, pause, stop).
  - Envio de dados de sensores (temperatura, umidade, etc.).
  - Configuração de parâmetros do processo.

- **Controle de Processo:**
  - Gerenciamento de atuadores.
  - Leitura de sensores em tempo real.
  - Salvamento de dados historizados.

- **Tarefas Assíncronas:**
  - Execução de tarefas em paralelo usando `asyncio`.

## Como Executar

Para executar este código no ESP32-C3, siga os passos abaixo:

### Pré-requisitos

- **Thonny IDE** instalado (ou outra IDE compatível com MicroPython).
- Um microcontrolador **ESP32** com **MicroPython** instalado.
- Conexão USB para upload do código e monitoramento serial.
- MALT-ESP instalado em um dispositivo android
  
  ```bash
   # Repositório MALT-ESP, mais informações no seu respectivo README
   git clone https://github.com/NicolasDezan/MALT-ESP.git
   ```
 

### Passos

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/NicolasDezan/ESP32C3-MaltingControl.git
   ```
   
2. **Abra o projeto no Thonny IDE:**
   - Conecte o ESP32-C3 ao computador via USB.
   - Abra o Thonny IDE e selecione o interpretador MicroPython para o ESP32.
   - Faça o upload da pasta projects dentro do ESP32.

3. **Execute o código:**
   - No Thonny, clique em **"Run"** para executar o código no ESP32-C3.
   - Monitore a saída no console serial para verificar o funcionamento.

4. **Conecte ao Bluetooth:**
   - Abra o aplicativo **MALT-ESP** no seu dispositivo Android.
   - Habilite o Bluetooth e conecte-se ao ESP32-C3.
   - Envie comandos e visualize os dados recebidos em tempo real.
