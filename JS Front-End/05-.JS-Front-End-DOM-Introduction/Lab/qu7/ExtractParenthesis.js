function extract(content) {
    let eleContent = document.getElementById(content).textContent;
    let matches = eleContent.match(/\([^)]+\)/g)
    
    if (matches) {
        return matches.join('; ')
    }
}

