class ActivityCategory {
  constructor(container = undefined, itemList = []) {
    this.container = container;
    this.itemList = this.createDraggables(itemList); // to be able to inject custom attributes

    console.log('positioning items');
    this.positionItems();

    if (! ActivityCategory.hasOwnProperty('containerReferences')) {
      ActivityCategory.containerReferences = {};
    }
    const key = container.attr('id');
    ActivityCategory.containerReferences[key] = this;
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
      TweenMax.to(item.origin, 0.6, {y: y_pos});
    });

  }

  createDraggable(item, delay) {
    const self = this;
    const d = Draggable.create(item, {
      type: 'x,y',
      bounds: window,

      /*
      A known bug would be when item is being dragged,
      it will only consider window bounds from the moment when dragging begins.
      A suggested solution is to update bounds when scrolling is detected!
      */
      onDragEnd: function() {
        /*
        check whether the item hit a different category
          if yes,
            then move the item to that category
            and make that category a variable
          else,
            move the item back to it's original position
        */

        // if category variable not set, check for self.container

        // check whether the item hit other item in the same category
          // if yes, we want to update order in the category
          // we also want to re-position all the items
      },
    })[0];

    d.origin = item;
    d.height = $(item).height();
    d.calculatePosition = function() {
      const my_index = self.itemList.indexOf(d);
      let position = 0;
      if (my_index > 0) {
        const prev_item_index = my_index - 1;
        const prev_item = self.itemList[prev_item_index];
        const h = prev_item.calculatePosition();
        return h + prev_item.height + 5;
      }
      return position;
    };
    return d;
  }

  createDraggables(itemList) {
    const self = this;
    const draggables_list = new Array();
    let d = 0;
    itemList.forEach(function(item) {
      const draggable = self.createDraggable(item, d);
      d += 0.5;
      draggables_list.push(draggable);
    });
    return draggables_list;
  }
}
