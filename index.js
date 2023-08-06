function submitform(e) {
    e.preventDefault();
    getData();

}

async function getData() {
    let userData = document.getElementById("input").value.trim();
    if (userData === "") return false;

    const API = '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'

    document.getElementById("messages").innerHTML = `<div class="mess-user"><p>${userData}</p></div>` + document.getElementById("messages").innerHTML;
    document.getElementById("input").value = ""
    try {
        const response = await fetch('https://api.openai.com/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${API}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                model: 'gpt-3.5-turbo',
                messages: [{ role: 'user', 'content': userData }],
                max_tokens: 100,
                temperature: 0.7,
                n: 1,

                timeout: 15

            })
        })

        const data = await response.json();
      
        document.getElementById("messages").innerHTML = `<div class="mess-chat"><p>${data.choices[0].message.content}</p></div>` + document.getElementById("messages").innerHTML;
        console.log(data)
     
      
    }
    catch (error) {
        console.error('Error', error)
    }
}