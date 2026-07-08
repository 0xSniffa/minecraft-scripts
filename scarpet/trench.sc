roundHalf(num) -> (
    return(round(num-0.5)+0.5)
);

notfinalPos = query(player(), 'Pos');
global_finalPos = [roundHalf(notfinalPos:0), floor(notfinalPos:1), roundHalf(notfinalPos:2)];
global_Rotation = query(player(), 'yaw');

// ---- config ----
waitTime = 300; // in ms
// ----------------

amount(angle1, angle2, positive, position, yaw) -> (
    {
        'angle1' -> angle1,
        'angle2' -> angle2,
        'positive' -> positive,
        'position' -> position,
        'yaw' -> yaw
        
    }
);

global_direction = [
    amount(  90,  135, -1, 1, 180), //'spawn West mine North'
    amount(-135,  -90,  1, 1, 180), //'spawn East mine North'
    amount(-180, -135, -1, 0, -90), //'spawn North mine East'
    amount( -45,    0,  1, 0, -90), //'spawn South mine East'
    amount(  45,   90, -1, 1,   0), //'spawn West mine South'
    amount( -90,  -45,  1, 1,   0), //'spawn East mine South'
    amount(   0,   45,  1, 0,  90), //'spawn South mine West'
    amount( 135,  180, -1, 0,  90)  //'spawn North mine West'
];

fspawn(name, count) -> (
    c_for(i=0, i<length(global_direction), i+=1,
        if(global_Rotation > global_direction:i:'angle1' && global_Rotation < global_direction:i:'angle2',
            looking = global_direction:i;
            c_for(j=0, j<count, j+=1,
                sleep(waitTime);
                run(str('player %s%d spawn at %d %d %d facing %d 45', name, j, global_finalPos:0+(j+1)*looking:'positive'*looking:'position', global_finalPos:1, global_finalPos:2+(j+1)*looking:'positive'*(1-looking:'position'), looking:'yaw'));
            );
            break();
        )
    )
);

__config() -> {
  'commands' -> {
    '<string> <int>' -> 'fspawn',
  }
};