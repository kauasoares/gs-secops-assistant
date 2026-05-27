import hashlib
import dns.resolver
import ipaddress

def analyze_password_strength(password: str) -> str:
    """Analisa a força e complexidade de uma senha (password)."""
    score = 0
    if len(password) >= 8: score += 1
    if len(password) >= 12: score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password): score += 1
    
    if score < 3: return "Fraca: Senha curta ou sem diversidade de caracteres. Vulnerável."
    elif score < 5: return "Média: Senha aceitável, mas pode ser melhorada com símbolos ou tamanho."
    else: return "Forte: Excelente complexidade de senha."

def generate_hash(text: str, algorithm: str = "sha256") -> str:
    """Gera o hash criptográfico de um texto utilizando o algoritmo especificado (md5, sha1, sha256)."""
    algo = algorithm.lower()
    try:
        if algo == 'md5':
            return hashlib.md5(text.encode()).hexdigest()
        elif algo == 'sha1':
            return hashlib.sha1(text.encode()).hexdigest()
        elif algo == 'sha256':
            return hashlib.sha256(text.encode()).hexdigest()
        else:
            return "Erro: Algoritmo não suportado. Use md5, sha1 ou sha256."
    except Exception as e:
        return f"Erro ao gerar hash: {str(e)}"

def check_dns_records(domain: str, record_type: str = "TXT") -> str:
    """Consulta registros DNS (como TXT, MX, A) de um domínio para auditoria de segurança (ex: google.com)."""
    try:
        answers = dns.resolver.resolve(domain, record_type)
        records = [str(rdata) for rdata in answers]
        return f"Registros {record_type} encontrados para {domain}:\n" + "\n".join(records)
    except Exception as e:
        return f"Erro ao consultar DNS ou registro '{record_type}' não encontrado para o domínio: {str(e)}"

def calculate_subnet(cidr: str) -> str:
    """Calcula informações de sub-rede a partir de um bloco CIDR (exemplo de entrada: 192.168.1.0/24)."""
    try:
        network = ipaddress.IPv4Network(cidr, strict=False)
        return (f"Endereço da Rede: {network.network_address}\n"
                f"Endereço de Broadcast: {network.broadcast_address}\n"
                f"Máscara de Sub-rede: {network.netmask}\n"
                f"Quantidade de Hosts utilizáveis: {network.num_addresses - 2}")
    except Exception as e:
        return f"Erro ao calcular sub-rede. Verifique se o formato CIDR está correto: {str(e)}"