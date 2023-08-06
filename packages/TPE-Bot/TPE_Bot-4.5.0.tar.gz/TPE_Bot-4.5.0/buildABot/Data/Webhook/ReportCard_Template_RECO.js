function recommendedMenu(agent){
  const hash = crypto.createHash('sha224');
  const string = agent.parameters.loginID;
  const hashedString = hash.update(string, 'utf-8');
  const gen_hash = hashedString.digest('hex');

  var id;
  var ref = admin.database().ref("ID");
  ref.orderByValue().equalTo(gen_hash).on("child_added", function(snapshot){
    id = snapshot.key;
  });
  
  return admin.database().ref().once("value").then(function(snapshot) {
    // name, grade, criterias 
    SNAPSHOTHERE

    // ASSIGNMENT GRADE HERE //
    var feedback = snapshot.child("/Feedback /"+id).val();

    agent.add('Hi ' + name + ' ! \n Your report card: ');
    feedbackPayload(agent, grade, feedback, CRITERIASHERE);
  });
}

function feedbackPayload(agent, grade, feedback, CRITERIASHERE){
  var flaw = 0; 
  HIGHLIGHTHERE
  if (criteria1 ==null NULLHERE){ //
    const buttonDefPayload = {
        "richContent": [
            [
            {
              "type": "description",
              "title": "Report Card",
              "text": [
                  'Grade :	' + grade , 
                  feedback
              ]
            },
            {
              "options": [
                {
                  "text": "See Topics"
                }
              ],
              "type": "chips"
            }
          ]
        ]
    };

    const payloadTele = {
      "telegram": {
      "text": "You can explore the menu too! 📂",
      "reply_markup": {
        "keyboard": [[{"text": "🔎 Learn & Explore","callback_data": "Learn & Explore"},{"text": "🖋 Results & Recommendation","callback_data": "Results & Recommendation"}]]
      }
    }
    };

    agent.add(new Payload(agent.UNSPECIFIED, buttonDefPayload, { rawPayload: true, sendAsMessage: true }));
    agent.add(new Payload(agent.TELEGRAM, payloadTele, { rawPayload: true, sendAsMessage: true }));
  }

  else{
    // IF LOOP //
    IFLOOPHERE
    const buttonPayload = {
      "richContent": [
        [
          {
            "type": "description",
            "title": "Report Card",
            "text": [
              'Grade : ' + grade ,
              feedback
            ]
          },
          {
              "options": [CHIPSPAYLOADHERE],
              "type": "chips"
          }
        ]
      ]
    };

    const payloadTele = {
      "telegram": {
      "text": "📂 Pick a topic:",
      "reply_markup": {
        "keyboard": [ TELEPAYLOADHERE ]
        }
      }
    };

    agent.add(new Payload(agent.UNSPECIFIED, buttonPayload, { rawPayload: true, sendAsMessage: true }));
    agent.add(new Payload(agent.TELEGRAM, payloadTele, { rawPayload: true, sendAsMessage: true }));
  }
}