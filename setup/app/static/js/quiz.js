console.log('yoo supp!');
function submitAnswers(answers){
    var choice = [];

//    for(var i = 0; i < answers.length; i++){
//        choice[i] = document.forms["quiz_form"]["q"+i].value;
//    }

    var results = document.getElementById('results');
	results.innerHTML = "<h3>You scored: <span></span> out of <span>" + answers.length+ "</span></h3>"

	return false;
}

function onSubmitAnswer(){
    console.log("hgjkl");

    return false;
}