function Palindrome() {
    const userInput = prompt("Введите слово для проверки:");

    if (!userInput) {
        console.log("Вы ничего не ввели");
        return;
    }

    const cleanedWord = userInput.toLowerCase().replace(/\s/g, '');
    const reversedWord = cleanedWord.split('').reverse().join('');

    if (cleanedWord === reversedWord) {
        console.log(`"${userInput}" является палиндромом!`);
    } else {
        console.log(`"${userInput}" не является палиндромом.`);
    }
}