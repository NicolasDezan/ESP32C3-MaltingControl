import gc

def print_memory_usage():
    # Habilita o garbage collector (caso não esteja habilitado)
    gc.enable()
    
    # Coleta lixo não utilizado (opcional, mas recomendado para uma medição mais precisa)
    gc.collect()
    
    # Obtém a memória alocada e a memória livre
    mem_alloc = gc.mem_alloc()
    mem_free = gc.mem_free()
    
    # Calcula a quantidade total de RAM disponível
    total_ram = mem_alloc + mem_free
    
    # Calcula a porcentagem de uso da RAM
    usage_percentage = (mem_alloc / total_ram) * 100
    
    # Exibe os resultados
    # print(f"Total de RAM: {total_ram} bytes")
    # print(f"RAM usada: {mem_alloc} bytes")
    # print(f"RAM livre: {mem_free} bytes")
    print(f"Usage RAM: {usage_percentage:.2f}%")
