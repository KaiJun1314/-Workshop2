let data = {
    "gallery": [
        {
            "image": "images/gallery_art/cafe_in_paris.jpg",
            "name": "Cafe In Paris",
            "author": "Gan Aik Tong"
        },
        {
            "image": "images/gallery_art/cozy_home.jpg",
            "name": "Cozy Home",
            "author": "Ahmad Zakii Anwar"
        },
        {
            "image": "images/gallery_art/house_in_white.jpg",
            "name": "House in White",
            "author": "Hassan Muthalib"
        },
        {
            "image": "images/gallery_art/national_palace_malaysia.jpg",
            "name": "National Palace Malaysia",
            "author": "Mohamed Zain Idris"
        },
        {
            "image": "images/gallery_art/time_portal.jpg",
            "name": "Time Portal",
            "author": "Syed Ahmad Jamal"
        }
    ]
};

//  Members data to be inserted.
let membersDOM = "";
// current teams
function getGallery() {
    document.getElementById("gallery-dev").innerHTML = `<h1 style="margin:90px auto">Loading Gallery ....</h1>`;
    if (data.gallery.length == 0) {
        membersDOM = `<h1 style="margin:90px auto">No Gallery Found</h1>`
    } else {
        for (let i = 0; i < data.gallery.length; i++) {
            let card = `<div class="col-xl-3 col-lg-4 col-md-6 mb-4">
        <div class="bg-white rounded shadow-sm"><a href="${data.gallery[i]}"
            data-lightbox="photos"><img src="${data.gallery[i].image}" alt="" class="img-fluid card-img-top">
          <div class="p-4">
            <h5> <a href="#" class="text-dark">${data.gallery[i].name}</a></h5>
            <p class="small text-muted mb-0">Create By: ${data.gallery[i].author}</p>
            </div>
          </div>
        </div>
      </div>`
            membersDOM += card;
        } 
    }
    document.getElementById("gallery-dev").innerHTML = membersDOM;
}
getGallery()