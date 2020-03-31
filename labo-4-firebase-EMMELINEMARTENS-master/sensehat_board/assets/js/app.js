const dbConfig = {
    collection: 'raspcollection',
    document: 'sensor-data'
};

const app = {
    init() {
        // initialiseer de firebase app
        firebase.initializeApp(firebaseConfig);
        this._db = firebase.firestore();
        // cache the DOM
        this.cacheDOMElements();
        this.cacheDOMEvents();

        this._matrix = {
            isOn: false, color: {value: '#000000', type: 'hex'}
        };
    },
    cacheDOMElements() {
        this.$colorPicker = document.querySelector('#colorPicker');
        this.$toggleMatrix = document.querySelector('#toggleMatrix');
        this.$btnChange = document.querySelector('#btnChange');
        this.$temperature = document.querySelector('#temperature');
        this.$humidity = document.querySelector('#humidity');
    },
    cacheDOMEvents() {
        this.$btnChange.addEventListener('click', (e) => {
            e.preventDefault();
            this._matrix.color.value = this.$colorPicker.value;
            this._matrix.isOn = this.$toggleMatrix.checked;

            this.updateInFirebase();
        });
    },
    updateInFirebase() {
        this._db.collection(dbConfig.collection).doc(dbConfig.document)
            .set(
                {matrix: this._matrix},
                {merge: true}
            );
    },
    readData() {
        /** constants */
        const temperature = document.getElementById('temperature');
        const humidity = document.getElementById('humidity');
    /** Ask for the data collection and loop the data */
    this._db.collection(dbConfig.collection).document(dbConfig.document)
    .onSnapShot((doc) => {
            temperature.innerText = `${parseFloat(doc.data().temperature).toFixed(2)}°C`;
            humidity.innerText = `${parseFloat(doc.data().humidity).toFixed(2)}`;
    })
    }
}

app.init();