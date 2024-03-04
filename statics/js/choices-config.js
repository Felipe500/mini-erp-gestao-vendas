if($('#id_produto_list').length){
		var select_produtos_list = new Choices('#id_produto_list', {
            removeItemButton: true,
            searchResultLimit:6,
            renderChoiceLimit:6,
            loadingText: 'Carregando...',
            noResultsText: 'Nenhum resultado encontrado',
            noChoicesText: 'Sem opções para escolher',
            itemSelectText: 'Pressione para selecionar',
            uniqueItemText: 'Somente valores exclusivos podem ser adicionados',
            customAddItemText: 'Somente valores correspondentes a condições específicas podem ser adicionados',
            renderSelectedChoices: 'null',
        });

}

if($('#id_categoria_list').length){
    var select_categoria_list = new Choices('#id_categoria_list', {
        removeItemButton: true,
        searchResultLimit:6,
        renderChoiceLimit:6,
        loadingText: 'Carregando...',
        noResultsText: 'Nenhum resultado encontrado',
        noChoicesText: 'Sem opções para escolher',
        itemSelectText: 'Pressione para selecionar',
        uniqueItemText: 'Somente valores exclusivos podem ser adicionados',
        customAddItemText: 'Somente valores correspondentes a condições específicas podem ser adicionados',
    });
}


if($('#id_cliente').length){
    var select_cliente_list = new Choices('#id_cliente', {
        removeItemButton: true,
        searchResultLimit:6,
        renderChoiceLimit:6,
        loadingText: 'Carregando...',
        noResultsText: 'Nenhum resultado encontrado',
        noChoicesText: 'Sem opções para escolher',
        itemSelectText: 'Pressione para selecionar',
        uniqueItemText: 'Somente valores exclusivos podem ser adicionados',
        customAddItemText: 'Somente valores correspondentes a condições específicas podem ser adicionados',
    });
}

if($('#id_cliente_readonly').length){
    var select_cliente_list = new Choices('#id_cliente_readonly', {
        removeItemButton: false,
        addItems: false,
        addItemFilter: null,
        removeItems: false,
        editItems: false,
        searchResultLimit:6,
        renderChoiceLimit:6,
        loadingText: 'Carregando...',
        noResultsText: 'Nenhum resultado encontrado',
        noChoicesText: 'Sem opções para escolher',
        itemSelectText: 'Pressione para selecionar',
        uniqueItemText: 'Somente valores exclusivos podem ser adicionados',
        customAddItemText: 'Somente valores correspondentes a condições específicas podem ser adicionados',
    });
}