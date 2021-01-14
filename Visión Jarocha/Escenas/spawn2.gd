extends Position2D


# Declare member variables here. Examples:
# var a = 2
#export (PackedScene) var cactus


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


func _on_Timer_timeout():
	$"../CACTUS2".global_position= global_position
	#newCactus.global_position= global_position
