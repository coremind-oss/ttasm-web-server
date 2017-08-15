class ActivityCategory {
  constructor(container = undefined, itemList = []) {
    this.container = container;
    this.itemList = itemList;
  }

  getItems() {
    return this.itemList;
  }

  moveItem(index, targetCategory) {
    const item = this.itemList[index]; // grab the item from the array
    this.itemList.splice(index, 1); // delete the item from the array
    targetCategory.addItem(item)
  }

  addItem(item) {
    this.itemList.push(item);
  }
}
