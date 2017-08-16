class ActivityCategory {
  constructor(container = undefined, itemList = []) {
    this.container = container;
    this.itemList = this.createDraggables(itemList); // to be able to inject custom attributes

    console.log('positioning items');
    this.positionItems();

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

  positionItems() {
    this.itemList.forEach(function(item) {
      const y_pos = item.calculatePosition();

      // TRY TO ANIMATE THESE ITEMS #2
      TweenMax.to(item, 1, {y: y_pos});
    });

  }

  createDraggable(item) {
    const self = this;
    const d = Draggable.create(item, {
      type: 'x,y',
      bounds: this.container,
    })[0];

    // TRY TO ANIMATE THESE ITEMS #1
    const result = TweenMax.to(d, 1, {x: 50, y: 150});
    console.warn(result);

    d.height = $(item).height();
    d.calculatePosition = function() {
      const my_index = self.itemList.indexOf(d);
      let position = 0;
      if (my_index > 0) {
        const prev_item_index = my_index - 1;
        const prev_item = self.itemList[prev_item_index];
        const h = prev_item.calculatePosition();
        return h + d.height;
      }
      return position;
    };
    return d;
  }

  createDraggables(itemList) {
    const self = this;
    const draggables_list = new Array();
    itemList.forEach(function(item) {
      const draggable = self.createDraggable(item);
      draggables_list.push(draggable);
    });
    return draggables_list;
  }
}
