function addFields(element) {
    let value = element.value;
    let container = document.getElementById("dynamic_input_field_container"); // Getelement where input field will added dynamically
  
    while (container.hasChildNodes()) {
      container.removeChild(container.lastChild);
    }
  
    if (value == "Website") {
      let div = document.createElement("div");
  
      div.innerHTML = `<div class="form-floating mb-3">
                          <input type="text" class="form-control" name="website_name" id="floatingInput"
                          placeholder="Website Name">
                          <label for="floatingInput" class="text-muted">Website Name</label>
                      </div>
                      <div class="form-floating mb-3">
                          <input type="text" class="form-control" name="website_url" id="floatingInput"
                          placeholder="Website Url">
                          <label for="floatingInput" class="text-muted">Website Url</label>
                      </div>
                      `;
      container.appendChild(div);
    } else if (value == "Desktop Application") {
      let div = document.createElement("div");
  
      div.innerHTML = `<div class="form-floating mb-3">
                          <input type="text" class="form-control" name="application_name" id="floatingInput"
                          placeholder="Application Name">
                          <label for="floatingInput" class="text-muted">Application Name</label>
                      </div>
                      `;
      container.appendChild(div);
    } else if (value == "Game") {
      let div = document.createElement("div");
  
      div.innerHTML = `<div class="form-floating mb-3">
                          <input type="text" class="form-control" name="game_name" id="floatingInput"
                          placeholder="Game Name">
                          <label for="floatingInput" class="text-muted">Game Name</label>
                      </div>
                      `;
      container.appendChild(div);
    }
  }
  
  
  
  function toggleView(id){
    const input = document.getElementById(`${id}`);
    const icon = document.getElementById(`icon-${id}`);
  
    if (input.type === "text" ){
      input.type = "password";
      icon.classList.remove("fa-eye");
      icon.classList.add("fa-eye-slash");
    }else{
      input.type = "text";
      icon.classList.remove("fa-eye-slash");
      icon.classList.add("fa-eye");
    }
  }