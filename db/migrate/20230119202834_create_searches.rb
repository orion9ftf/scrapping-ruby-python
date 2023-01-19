class CreateSearches < ActiveRecord::Migration[7.0]
  def change
    create_table :searches do |t|
      t.text :title
      t.text :rut

      t.timestamps
    end
  end
end
