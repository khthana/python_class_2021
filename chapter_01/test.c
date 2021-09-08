/*This is the code to show numerals 0 to 9 on a 7 segment LED display It represents seconds*/

//bits representing numerals 0-9
const byte numeral[11] = {
  B11111100, //0
  B01100000, //1
  B11011010, //2
  B11110010, //3
  B01100110, //4
  B10110110, //5
  B00111110, //6
  B11100000, //7
  B11111110, //8
  B11100110, //9
  B00000000, //shows nothing
};

const byte hooray_bit[10] = {
  B10000000, //0
  B01000000, //1
  B00100000, //2
  B00010000, //3
  B00001000, //4
  B00000100, //5
  B00000010, //6
  B00000000, //shows nothing
};

//pins for each segment (g-a) on the 7 segment LED display with the corresponding arduino connection
//                            .  g  f   e  d  c  b   a
const int segmentPins[8] =   {8, 9, 10, 5, 6, 7, 12, 11};
const int GUESS_BUTTON_PIN = 2;
const int START_BUTTON_PIN = 4;

const int led_delay = 50;

const unsigned int DEBOUNCE_DELAY = 120;

boolean start_state;
boolean guess_state;

int random_no = 0;
int guess = 0;

void random_show() {
  boolean isBitSet;

  output_result(10);
  for (int t = 0; t < 3; t++) {
    for (int n = 0; n < 9; n++) {
      for (int segment = 0; segment < 8; segment++)
      {
        isBitSet = bitRead(hooray_bit[n], segment);
        digitalWrite(segmentPins[segment], isBitSet);
        delay(10);
      }
    }
  }
  output_result(10);
}

void setup()
{
  for (int i = 0; i < 8; i++)
  {
    pinMode(segmentPins[i], OUTPUT);
  }
  pinMode(GUESS_BUTTON_PIN, INPUT);
  pinMode(START_BUTTON_PIN, INPUT);
  randomSeed(analogRead(A0));
  random_no = random(1, 10);
  Serial.begin(9600);
  Serial.println(random_no);
  //random_show();
}

boolean debounce(int pin)
{
  boolean state;
  boolean previousState;
  previousState = digitalRead(pin); // store switch state
  for (int counter = 0; counter < DEBOUNCE_DELAY; counter++)
  {
    delay(1); // wait for 1 millisecond
    state = digitalRead(pin); // read the pin
    if ( state != previousState)
    {
      counter = 0; // reset the counter if the state changes
      previousState = state; // and save the current state
    }
  }
  // here when the switch state has been stable longer than the debounce period
  return state;
}


void output_result (int number)
{
  boolean isBitSet;

  for (int segment = 0; segment < 8; segment++)
  {
    isBitSet = bitRead(numeral[number], segment);
    digitalWrite(segmentPins[segment], !isBitSet);
  }
}

void handle_guess_button() {
  guess_state = debounce(GUESS_BUTTON_PIN);
  if (guess_state == LOW) {
    guess = guess + 1;
    if (guess >= 10) guess = 1;
    output_result(guess);
    Serial.println(guess);
  }
}

void hooray() {
  boolean isBitSet;
  for (int n = 0; n < 6; n++) {
    for (int segment = 0; segment < 8; segment++)
    {
      isBitSet = bitRead(0b11101110, segment);
      digitalWrite(segmentPins[segment], isBitSet);
      delay(100);
    }

  }
  output_result(10);
}

void greater() {
  // display G
  boolean isBitSet;
  for (int n = 0; n < 6; n++)
  {
    for (int segment = 0; segment < 8; segment++)
    {
      isBitSet = bitRead(0b10111100, segment);
      digitalWrite(segmentPins[segment], isBitSet);
      delay(100);
    }
  }
}

void lower() {
  // display L
  boolean isBitSet;
  for (int n = 0; n < 6; n++) {
    for (int segment = 0; segment < 8; segment++)
    {
      isBitSet = bitRead(0b00011100, segment);
      digitalWrite(segmentPins[segment], isBitSet);
      delay(100);
    }
  }
}

void handle_start_button() {
  start_state = debounce(START_BUTTON_PIN);

  if (start_state == LOW)
  {
    delay(1000);
    if (random_no == guess)
    {
      hooray();
    }
    else if (random_no < guess)
    {
      greater();
    }
    else
    {
      lower();
    }
  }
  delay(1000);
  guess = 0;
}

void loop()
{
  handle_guess_button();
  handle_start_button();
}








