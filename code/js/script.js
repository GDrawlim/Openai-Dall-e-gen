

const reqButton = document.getElementById('button-request');

console.log(reqButton);

reqButton.onclick = function() {
    const key = document.getElementById('api-key').value;
    const prompt = document.getElementById('text-prompt').value;
    const count = (document.getElementById('image-count').value);
    const radios = document.getElementsByName('image-size')
    let size;
    for (let i=0;i< radios.length; i++)
    {
        if (radios[i].checked)
        {
            size= Number(radios[i].value);
            break;
        }
        
    }
    const reqBody = {
        prompt: prompt,
        n: count,
        size: size + "x" + size,
        response_format: "url"
    }


    console.log(reqBody);
}