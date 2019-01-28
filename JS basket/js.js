"use strict";

const basket = {
  settings: {
    countSelector: '#basket-count',
    priceSelector: '#basket-price',
    btnSelector1: '.buy-btn-1',
    btnSelector2: '.buy-btn-2',
    btnSelector3: '.buy-btn-3',
  },
  goods: [],
  countEl: null,
  priceEl: null,
  sumPrice: 0,

  init(userSettings = {}) {
    Object.assign(this.settings, userSettings);
    document
      .querySelector(this.settings.btnSelector1)
      .addEventListener('click', event => this.add(event.target.dataset.name, event.target.dataset.price));

    document
      .querySelector(this.settings.btnSelector2)
      .addEventListener('click', event => this.add(event.target.dataset.name, event.target.dataset.price));

    document
      .querySelector(this.settings.btnSelector3)
      .addEventListener('click', event => this.add(event.target.dataset.name, event.target.dataset.price));
  },

  add(goodName, goodPrice) {
    // передаем спан куда вставлять.
    this.priceEl = document.querySelector(this.settings.priceSelector);
    // увеличиваем общую сумму после каждого клика.
    this.sumPrice = this.sumPrice + +(goodPrice);
    // записываем в span
    this.priceEl.innerHTML = this.sumPrice;

    // добавляем в массив "купленные" товары.
    this.goods.push(goodName);
    // передаем спан куда вставлять.
    this.countEl = document.querySelector(this.settings.countSelector);
    // подсчитываем длинну массива с товарами и передаём в спан.
    this.countEl.innerHTML = this.goods.length;
  },
};

window.onload = () => basket.init();