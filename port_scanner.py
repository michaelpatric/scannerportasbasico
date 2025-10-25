import socket
import sys

def scan_port(host, port):
    """Tenta conectar-se à porta para verificar se está aberta."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5) # Define um tempo limite de 0.5 segundos para a conexão
    
    try:
        # Se a conexão for bem-sucedida, a porta está aberta
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Porta {port}: ABERTA")
        else:
            # Ocultar portas fechadas para um output mais limpo
            pass
            
    except socket.gaierror:
        print(f"Erro: O nome do host '{host}' não pôde ser resolvido.")
        sys.exit()
    except socket.error:
        print(f"Erro: Não foi possível conectar ao servidor.")
        sys.exit()
    finally:
        sock.close()

if __name__ == "__main__":
    
    # Define o alvo
    target_host = input("Digite o host ou IP alvo (ex: scanme.nmap.org): ")
    
    # Define a faixa de portas (vamos começar com as 100 portas mais comuns)
    start_port = 1
    end_port = 100
    
    print("-" * 50)
    print(f"Iniciando varredura em {target_host}...")
    print(f"Verificando portas de {start_port} a {end_port}")
    print("-" * 50)
    
    for port in range(start_port, end_port + 1):
        scan_port(target_host, port)
        
    print("-" * 50)
    print("Varredura concluída.")