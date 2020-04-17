// const handleImageUpload = event => {
//     const files = event.target.files
//     const formData = new FormData()
//     formData.append('myFile', files[0])
  
//     fetch('/saveImage', {
//       method: 'POST',
//       body: formData
//     })
//     .then(response => response.json())
//     .then(data => {
//       console.log(data.path)
//     })
//     .catch(error => {
//       console.error(error)
//     })
//   }
  
//   document.querySelector('#img').addEventListener('change', event => {
//     handleImageUpload(event)
//   })

var button = document.getElementsById('button')

button.addEventListner('click',function(e){
    var textarea = document.getElementsById('img').value
    
    download(textarea)
})

function download(textarea){
    var element = document.createElement('a')
    element.setAttribute('href', 'data:Image');
    element.setAttribute('download');
    element
}